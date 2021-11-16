SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


DROP DATABASE IF EXISTS `project`;
CREATE DATABASE `project`;
USE `project`;


# Create TABLE 'CreditLevel'
CREATE TABLE `CreditLevel` (
  `credit_level` int NOT NULL,
  `loan_amount` int NOT NULL,
  PRIMARY KEY (credit_level)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CreditLevel` WRITE;
/*!40000 ALTER TABLE `CreditLevel` DISABLE KEYS */;
INSERT INTO `CreditLevel` VALUES (1, 5000);
INSERT INTO `CreditLevel` VALUES (2, 12000);
INSERT INTO `CreditLevel` VALUES (3, 20000);
/*!40000 ALTER TABLE `CreditLevel` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'User'
CREATE TABLE `User` (
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `credit_level` int NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (credit_level) REFERENCES CreditLevel(credit_level)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (-1, "Bank", 3);
INSERT INTO `User` VALUES (1, "Dennis", 3);
INSERT INTO `User` VALUES (2, "Lisa", 2);
INSERT INTO `User` VALUES (3, "Joe", 1);
INSERT INTO `User` VALUES (4, "Rick", 2);
INSERT INTO `User` VALUES (5, "Tim", 3);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'LoginTime'
CREATE TABLE `LoginTime` (
  `user_id` int NOT NULL,
  `login_time` DATETIME NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `LoginTime` WRITE;
/*!40000 ALTER TABLE `LoginTime` DISABLE KEYS */;
INSERT INTO `LoginTime` VALUES (1, '2021-10-24 10:28:36');
INSERT INTO `LoginTime` VALUES (2, '2021-10-24 12:10:54');
INSERT INTO `LoginTime` VALUES (3, '2021-10-24 15:47:02');
INSERT INTO `LoginTime` VALUES (4, '2021-10-24 16:03:21');
INSERT INTO `LoginTime` VALUES (5, '2021-10-24 20:58:33');
INSERT INTO `LoginTime` VALUES (3, '2021-10-25 09:15:27');
INSERT INTO `LoginTime` VALUES (2, '2021-10-27 22:52:51');
INSERT INTO `LoginTime` VALUES (5, '2021-10-28 19:43:09');
/*!40000 ALTER TABLE `LoginTime` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Account'
CREATE TABLE `Account` (
  `user_id` int NOT NULL,
  `account_id` int NOT NULL,
  `currency_type` varchar(10) NOT NULL,
  `balance` int NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES (-1, 1, 'HKD', -1);
INSERT INTO `Account` VALUES (1, 1, 'HKD', 55000);
INSERT INTO `Account` VALUES (1, 2, 'HKD', 2500);
INSERT INTO `Account` VALUES (1, 3, 'USD', 800);
INSERT INTO `Account` VALUES (1, 4, 'CNY', 1600);
INSERT INTO `Account` VALUES (2, 1, 'HKD', 5200);
INSERT INTO `Account` VALUES (2, 2, 'HKD', 100000);
INSERT INTO `Account` VALUES (2, 3, 'USD', 50000);
INSERT INTO `Account` VALUES (2, 4, 'CNY', 100000000);
INSERT INTO `Account` VALUES (3, 1, 'HKD', 1000);
INSERT INTO `Account` VALUES (3, 2, 'HKD', 5000);
INSERT INTO `Account` VALUES (3, 3, 'USD', 5000);
INSERT INTO `Account` VALUES (3, 4, 'CNY', 1490);
INSERT INTO `Account` VALUES (4, 1, 'HKD', 5000);
INSERT INTO `Account` VALUES (4, 2, 'HKD', 10000);
INSERT INTO `Account` VALUES (4, 3, 'USD', 1500);
INSERT INTO `Account` VALUES (4, 4, 'CNY', 25000);
INSERT INTO `Account` VALUES (5, 1, 'HKD', 5000);
INSERT INTO `Account` VALUES (5, 2, 'HKD', 1600);
INSERT INTO `Account` VALUES (5, 3, 'USD', 3000);
INSERT INTO `Account` VALUES (5, 4, 'CNY', 1050);
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Transaction'
CREATE TABLE `Transaction` (
  `transaction_id` int NOT NULL,
  `from_user` int NOT NULL,
  `to_user` int NOT NULL,
  `from_account` int NOT NULL,
  `to_account` int NOT NULL,
  `currency_type` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `transaction_time` DATETIME NOT NULL,

  PRIMARY KEY (transaction_id),
  FOREIGN KEY (from_user) REFERENCES User(user_id),
  FOREIGN KEY (to_user) REFERENCES User(user_id)

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Transaction` WRITE;
/*!40000 ALTER TABLE `Transaction` DISABLE KEYS */;
INSERT INTO `Transaction` VALUES (1, 4, 1, 1, 1, 'HKD', 200, '2021-10-24 16:05:33');
INSERT INTO `Transaction` VALUES (2, 5, 3, 1, 2, 'HKD', 1000, '2021-10-24 21:00:04');
INSERT INTO `Transaction` VALUES (3, 2, 1, 1, 1, 'HKD', 50, '2021-10-27 22:52:51');
INSERT INTO `Transaction` VALUES (4, 1, 3, 1, 1, 'HKD', 200, '2021-10-20 19:05:30');
INSERT INTO `Transaction` VALUES (5, 2, 5, 4, 4, 'CNY', 200, '2021-10-21 09:05:04');
INSERT INTO `Transaction` VALUES (6, 4, 3, 1, 1, 'HKD', 50, '2021-10-29 10:15:30');
INSERT INTO `Transaction` VALUES (7, 4, 1, 3, 3, 'USD', 150, '2021-10-14 15:45:19');
INSERT INTO `Transaction` VALUES (8, 5, 3, 1, 1, 'HKD', 500, '2021-10-24 18:05:33');
INSERT INTO `Transaction` VALUES (9, 1, 5, 4, 4, 'CNY', 500, '2021-09-28 06:15:30');
INSERT INTO `Transaction` VALUES (10, 2, 3, 1, 1, 'HKD', 500, '2021-10-13 08:05:34');
INSERT INTO `Transaction` VALUES (11, 3, 1, 3, 3, 'USD', 20, '2021-10-30 06:25:39');
/*!40000 ALTER TABLE `Transaction` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Loan'
CREATE TABLE `Loan` (
  `user_id` int NOT NULL,
  `loan_id` int NOT NULL,
  `loan_amount` int NOT NULL,
  `apply_date` DATE NOT NULL,
  `due_date` DATE NOT NULL,
  `is_settled` INT,
  `settle_date` DATE,
  FOREIGN KEY (user_id) REFERENCES User(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Loan` WRITE;
/*!40000 ALTER TABLE `Loan` DISABLE KEYS */;
INSERT INTO `Loan` VALUES (1, 1, 5200, '2021-10-14', '2021-10-24', 1, '2021-10-22');
INSERT INTO `Loan` VALUES (1, 2, 2000, '2021-10-10', '2021-10-25', 1, '2021-10-24');
INSERT INTO `Loan` VALUES (1, 3, 4000, '2021-11-09', '2021-11-29', 0, NULL);
INSERT INTO `Loan` VALUES (3, 1, 380, '2021-10-20', '2021-10-28', 1, '2021-10-28');
INSERT INTO `Loan` VALUES (5, 1, 5500, '2021-10-25', '2021-12-25', 0, NULL);
/*!40000 ALTER TABLE `Loan` ENABLE KEYS */;
UNLOCK TABLES;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
