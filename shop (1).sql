-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 13, 2021 at 09:28 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `sno` int(200) NOT NULL,
  `categoryName` varchar(200) NOT NULL,
  `seller` varchar(200) NOT NULL,
  `categoryNumber` varchar(200) NOT NULL,
  `active` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`sno`, `categoryName`, `seller`, `categoryNumber`, `active`) VALUES
(3, 'Mud Cake', 'artsy', '2', '1'),
(4, 'Choclate Cake', 'artsy', '3', '1'),
(5, 'Mud Cake', 'cakes', '1', '1'),
(6, 'Mud Cake', 'crafts&bakes', '11', '1'),
(7, 'Cream Cake', 'artsy', '12', '1'),
(10, 'Ice Cream Cake', 'artsy', '15', '1'),
(12, 'Cream Cake', 'cakes', '1', '1'),
(13, 'Choclate Cake', 'cakes', '12', '1'),
(14, 'Ice Cream Cake', 'cakes', '43', '1'),
(15, 'Cream Cake', 'crafts&bakes', '12', '1'),
(16, 'Cream Cake', 'artsy', '43', '0');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `sno` int(11) NOT NULL,
  `product_id` varchar(12) DEFAULT NULL,
  `product_name` varchar(500) DEFAULT NULL,
  `product_seller` varchar(200) DEFAULT NULL,
  `product_price` varchar(200) NOT NULL,
  `total_order` varchar(200) NOT NULL,
  `full_address` varchar(200) NOT NULL,
  `payment_method` varchar(30) NOT NULL,
  `user_name` varchar(200) DEFAULT NULL,
  `user_mobile` varchar(200) DEFAULT NULL,
  `user_email` varchar(200) DEFAULT NULL,
  `active` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`sno`, `product_id`, `product_name`, `product_seller`, `product_price`, `total_order`, `full_address`, `payment_method`, `user_name`, `user_mobile`, `user_email`, `active`) VALUES
(1, NULL, NULL, NULL, '', '', 'qerfdsfsd', 'Bikash', NULL, NULL, NULL, ''),
(2, '1', NULL, NULL, '', '', 'aasasas', 'roket', NULL, NULL, NULL, ''),
(3, '1', NULL, NULL, '', '', 'ssddddd', 'Bikash', NULL, NULL, NULL, ''),
(4, '1', NULL, NULL, '', '', 'ssddddd', 'Bikash', NULL, NULL, NULL, ''),
(5, '1', 'Bg', NULL, '', '', 'gffgfgf', 'Bikash', NULL, NULL, NULL, ''),
(6, '1', 'Bg', NULL, '', '', 'dfdfd', 'Bikash', NULL, NULL, NULL, ''),
(7, '1', 'Bg', NULL, '', '', 'sadfdafdf', 'Bikash', 'Mizan', '01862856218', 'mizan@gmail.com', ''),
(8, '2', 'pizza', NULL, '', '', 'Sss', 'Bikash', 'Mizan', '01862856218', 'mizan@gmail.com', ''),
(9, '2', 'pizza', 'seller2', '', '', 'XZxzxzx', 'cash on delivery', 'Mizan', '01862856218', 'mizan@gmail.com', ''),
(10, '1', 'Bg', 'seller1', '', '', '', 'cash on delivery', 'Mizan', '01862856218', 'mizan@gmail.com', ''),
(11, '1', 'Bg', 'seller1', '', '', 'rhrrrh', 'Bikash', 'esha', '01862856218', 'esha@gmail.com', ''),
(12, '1', 'Bg', 'artsy', '', '', 'mirsaray', 'Bikash', 'Mizan', '01862856218', 'mizan@gmail.com', '1'),
(14, '10', 'Buttercream floral cake.', 'mizan', '', '', 'marium nagar,Rangunia,chittagong', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '1'),
(15, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(16, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(17, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(18, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(19, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(20, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(21, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(22, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(23, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(24, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(25, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '1'),
(26, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '1'),
(27, '7', 'Yellow', 'artsy', '2000', '2', 'aefadfdsf', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '1'),
(28, '10', 'Buttercream floral cake.', 'crafts&bakes', '30000', '10', '', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(29, '10', 'Buttercream floral cake.', 'crafts&bakes', '6000', '2', 'sdsds', 'cash on delivery', 'Esha', '01862856218', 'esha@gmail.com', '0'),
(30, '9', 'Butter cream floral cake', 'cakes', '3500', '5', 'marium nagar,Rangunia,chittagong', 'Bikash', 'Esha', '01862856218', 'esha@gmail.com', '0');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `sno` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `seller` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `active` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`sno`, `name`, `slug`, `image`, `price`, `seller`, `category`, `description`, `date`, `active`) VALUES
(7, 'Yellow', 'Yellow', 'cake10.jpg', '1000', 'artsy', 'Cream', 'Nice', '2021-03-15 20:38:35.276983', '1'),
(8, 'Cartoon', 'Cartoon', 'cake11.jpg', '500', 'artsy', 'Mud', '', '2021-03-15 20:41:25.549371', '1'),
(9, 'Butter cream floral cake', 'Butter cream floral cake', 'Butter cream floral cake.JPG', '700', 'cakes', 'Mud Cake', '', '2021-03-15 20:43:39.522979', '1'),
(10, 'Buttercream floral cake.', 'Buttercream floral cake.', 'Buttercream floral cake.JPG', '3000', 'crafts&bakes', 'Mud Cake', '', '2021-03-15 20:46:23.711877', '1'),
(12, 'asas', 'asas', 'cake5.jpeg', '700', 'artsy', 'Mud', 'Nice', '2021-03-16 16:03:37.240626', '1'),
(15, 'cake1', 'cake1', 'cake3.jpg', '700', 'cakes', 'Cream', 'dsdsdsds', '2021-03-17 17:56:27.321201', '1'),
(16, 'cake2', 'cake2', 'cake2.jpg', '500', 'cakes', 'Mud', 'saddds', '2021-03-17 17:57:01.614511', '1'),
(17, 'cake4', 'cd', 'cake4.jpeg', '500', 'cakes', 'Cream', 'scdd', '2021-03-17 18:03:15.356493', '1');

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

CREATE TABLE `seller` (
  `id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seller`
--

INSERT INTO `seller` (`id`, `name`, `username`, `password`, `phone`, `email`, `image`) VALUES
(1, 'Artsy', 'artsy', '12345', '0121020120', 'artsy@gmail.com', 'artsy.JPG'),
(2, 'cakes', 'cakes', '5255', '112121212', 'Cakes@gmail.com', 'cakes.JPG'),
(3, 'crafts&bakes', 'crafts&bakes', '54321', '121322223233', 'Cakes@gmail.com', 'crafts.JPG');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `sno` int(200) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `image` varchar(200) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`sno`, `first_name`, `last_name`, `email`, `mobile`, `image`, `password`) VALUES
(11, 'Sayama', 'Esha', 'esha@gmail.com', '01862856218', 'esha.jpeg', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `seller`
--
ALTER TABLE `seller`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `seller`
--
ALTER TABLE `seller`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
