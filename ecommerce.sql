-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2023 at 10:18 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `desc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`name`, `type`, `img`, `price`, `desc`) VALUES
('apple', 'cloth', 'static/file/download.jpeg', '50', 'apple'),
('cloth', 'cloth', 'static/file/clothes.jpg', '500', 'clothes'),
('mobile', 'mobile', 'static/file/mobile.jpeg', '100000', 'mobile phone'),
('shoe', 'shoe', 'static/file/shoe.jpeg', '250', 'shoe'),
('Laptop', 'laptop', 'static/file/pexels-karsten-madsen-18105.jpg', '50000', 'Laptop');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `name` varchar(100) NOT NULL,
  `prod_name` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `dept` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `value` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uses`
--

CREATE TABLE `uses` (
  `name` int(11) NOT NULL,
  `gender` int(11) NOT NULL,
  `mail` int(11) NOT NULL,
  `phone` int(11) NOT NULL,
  `password` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `uses`
--

INSERT INTO `uses` (`name`, `gender`, `mail`, `phone`, `password`) VALUES
(0, 0, 0, 2147483647, 123),
(0, 0, 0, 2147483647, 123),
(0, 0, 0, 2147483647, 123),
(0, 0, 0, 2147483647, 123),
(0, 0, 0, 2147483647, 0),
(0, 0, 0, 2147483647, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
