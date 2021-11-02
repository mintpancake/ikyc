-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--
DROP TABLE IF EXISTS `Customer`;

# Create TABLE 'User'
CREATE TABLE `User` (
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1, "Dennis");
INSERT INTO `User` VALUES (2, "Lisa");
INSERT INTO `User` VALUES (3, "Joe");
INSERT INTO `User` VALUES (4, "Rick");
INSERT INTO `User` VALUES (5, "Tim");
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

# Create TABLE 'Login'
CREATE TABLE `LoginTime` (
  `user_id` int NOT NULL,
  `login_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
INSERT INTO `Login` VALUES (1, '2021-10-24-10-28-36');
INSERT INTO `Login` VALUES (2, '2021-10-24-12-10-54');
INSERT INTO `Login` VALUES (3, '2021-10-24-15-47-02');
INSERT INTO `Login` VALUES (4, '2021-10-24-16-03-21');
INSERT INTO `Login` VALUES (5, '2021-10-24-20-58-33');
INSERT INTO `Login` VALUES (3, '2021-10-25-09-15-27');
INSERT INTO `Login` VALUES (2, '2021-10-27-22-52-51');
INSERT INTO `Login` VALUES (5, '2021-10-28-19-43-09');
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;

# Create TABLE 'Account'
CREATE TABLE `Account` (
  `user_id` int NOT NULL,
  `account_id` int NOT NULL,
  `type` varchar(10) NOT NULL,
  `balance` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES (1, 1, 'HKD', 550);
INSERT INTO `Account` VALUES (2, 1, 'HKD', 2500);
INSERT INTO `Account` VALUES (3, 1, 'USD', 800);
INSERT INTO `Account` VALUES (3, 2, 'HKD', 1600);
INSERT INTO `Account` VALUES (4, 1, 'HKD', 5200);
INSERT INTO `Account` VALUES (5, 1, 'HKD', 100000);
INSERT INTO `Account` VALUES (5, 2, 'USD', 50000);
INSERT INTO `Account` VALUES (5, 3, 'RMB', 1000000000);

/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

# Create TABLE 'Transaction'
CREATE TABLE `Transaction` (
  `transaction_id` int NOT NULL,
  `from_user` int NOT NULL,
  `to_user` int NOT NULL,
  `from_account` int NOT NULL,
  `to_account` int NOT NULL,
  `current_type` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `transaction_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Transaction` WRITE;
/*!40000 ALTER TABLE `Transaction` DISABLE KEYS */;
INSERT INTO `Transaction` VALUES (1, 4, 1, 1, 1, 'HKD', 200, '2021-10-24-16-05-33');
INSERT INTO `Transaction` VALUES (2, 5, 3, 1, 2, 'HKD', 1000, '2021-10-24-21-00-04');
INSERT INTO `Transaction` VALUES (3, 2, 1, 1, 1, 'HKD', 50, '2021-10-27-22-52-51');

/*!40000 ALTER TABLE `Transaction` ENABLE KEYS */;
UNLOCK TABLES;

# Create TABLE 'Friend'
CREATE TABLE `Friend` (
  `user_id1` int NOT NULL,
  `user_id2` int NOT NULL,
  `established_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Friend` WRITE;
/*!40000 ALTER TABLE `Friend` DISABLE KEYS */;
INSERT INTO `Friend` VALUES (1, 5, '2021-10-24');
INSERT INTO `Friend` VALUES (2, 3, '2021-10-24');
INSERT INTO `Friend` VALUES (2, 4, '2021-10-24');
INSERT INTO `Friend` VALUES (1, 3, '2021-10-25');

/*!40000 ALTER TABLE `Friend` ENABLE KEYS */;
UNLOCK TABLES;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
