import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/fogg-4075-bk-elegant-design-analog-watch-men/product-reviews/itm442cfc78a97b3?pid=WATFZ9UDHFAMUWMM&lid=LSTWATFZ9UDHFAMUWMMF3OWGH&marketplace=FLIPKART'

page_response = requests.get(url, timeout=240)
page_content = BeautifulSoup(page_response.content, "html.parser")
mydivs = page_content.find_all("div", {"class": "_6K-7Co"})

for i in mydivs:
    print(i)