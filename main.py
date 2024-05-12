from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle

UPLOAD_FOLDER = 'static/file/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="ecommerce")
mycursor = mydb.cursor(buffered=True)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def login():
    return render_template('login.html')

@app.route('/admin')
def login1():
    return render_template('login1.html')

@app.route('/reg')
def reg():
    return render_template('user_reg.html')

@app.route('/validate', methods=['POST', 'GET'])
def validate():
    global uname
    global upass
    if request.method == 'POST':
        uname = request.form.get('username')
        upass = request.form.get('password')
        sql = 'SELECT * FROM `uses` WHERE `name` = %s AND `password` = %s'
        val = (uname, upass)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            return redirect(url_for('user_dash'))
        else:
            return render_template('login.html', msg='Invalid Data')

@app.route('/ad_validate', methods=['POST', 'GET'])
def ad_validate():
    if request.method == 'POST':
        uname = request.form.get('username')
        upass = request.form.get('password')
        if uname == 'admin1' and upass == '1234':
            return redirect(url_for('admin_dash'))
        else:
            return render_template('login1.html', msg='Invalid')
    elif request.method == 'GET':
        return render_template('login1.html', msg='Please login')

@app.route('/admin_dash')
def admin_dash():
    return render_template('admin_dash.html')

@app.route('/user_dash')
def user_dash():
    sql = 'SELECT * FROM `products`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if result:
        return render_template('dashboard.html', data=result)
    else:
        return render_template('dashboard.html', msg='No Products')

@app.route('/view')
def view():
    sql = 'SELECT * FROM `products`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if result:
        return render_template('view.html', data=result)
    else:
        return render_template('view.html', msg='No Data')

@app.route('/add_prod', methods=['POST', 'GET'])
def add_prod():
    if request.method == 'POST':
        name = request.form.get('name')
        prod_type = request.form.get('prod_type')
        img = request.files['img']
        price = request.form.get('price')
        desc = request.form.get('desc')
        prod_img = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(prod_img)
        sql = 'INSERT INTO `products` (`name`, `type`, `img`, `price`, `desc`) VALUES (%s, %s, %s, %s, %s)'
        val = (name, prod_type, prod_img, price, desc)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('admin_dash.html', msg='Product Added')

@app.route('/userreg', methods=['POST', 'GET'])
def userreg():
    if request.method == 'POST':
        name = request.form.get('username')
        gender = request.form.get('gender')
        mail = request.form.get('mail')
        phone = request.form.get('phone')
        password = request.form.get('password')
        sql = "INSERT INTO uses (`name`, `gender`, `mail`, `phone`, `password`) VALUES (%s, %s, %s, %s, %s)"
        val = (name, gender, mail, phone, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('login.html')

@app.route('/review_page', methods=['POST', 'GET'])
def review_page():
    if request.method == 'POST':
        name = request.form.get('product')
        sql = 'SELECT * FROM `products` WHERE `name` = %s'
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return render_template('review.html', data=result)

@app.route('/add_review', methods=['POST', 'GET'])
def add_review():
    if request.method == 'POST':
        prod_name = request.form.get('prod_name')
        review = request.form.get('review')
        rating = request.form.get('rating')

        df = pd.read_csv('deceptive-opinion.csv')
        df1 = df[['deceptive', 'text']]
        df1.loc[df1['deceptive'] == 'deceptive', 'deceptive'] = 0
        df1.loc[df1['deceptive'] == 'truthful', 'deceptive'] = 1
        X = df1['text']
        Y = np.asarray(df1['deceptive'], dtype=int)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=109)
        cv = CountVectorizer()
        x = cv.fit_transform(X_train)
        y = cv.transform(X_test)

        data = [review]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
        ans = pred[0]
        if ans == 1:
            status = 'Real'
        else:
            status = 'Fake'

        v = 0

        sql = 'SELECT `type` FROM `products` WHERE `name` = %s'
        val = (prod_name,)
        mycursor.execute(sql, val)
        result1 = mycursor.fetchone()
        sql = 'INSERT INTO `reviews` (`name`, `prod_name`, `review`, `rating`, `dept`, `status`, `value`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        val = (uname, prod_name, review, rating, result1[0], status, v)
        mycursor.execute(sql, val)
        mydb.commit()

        if status == 'Fake':
            return render_template('review.html', msg='Review Added', script='showWarningPopup();')
        else:
            return render_template('review.html', msg='Review Added')

@app.route('/review')
def review():
    sql = 'SELECT * FROM `reviews`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if result:
        return render_template('admin_review.html', data=result)
    else:
        return render_template('admin_review.html', msg='No Reviews')

@app.route('/usereview')
def userreview():
    sql = 'SELECT * FROM `reviews`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if result:
        return render_template('userreview.html', data=result)
    else:
        return render_template('review.html', msg='No Reviews')


if __name__ == '__main__':
    app.run(debug=True, port=3004)
