DROP DATABASE IF EXISTS `ikyc`;
CREATE DATABASE `ikyc`;
USE `ikyc`;

CREATE TABLE `User` (
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `User` WRITE;
INSERT INTO `User` VALUES (1, "Dennis");
INSERT INTO `User` VALUES (2, "Lisa");
INSERT INTO `User` VALUES (3, "Joe");
INSERT INTO `User` VALUES (4, "Rick");
INSERT INTO `User` VALUES (5, "Tim");
UNLOCK TABLES;

CREATE TABLE `Login` (
  `user_id` int NOT NULL,
  `login_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Login` WRITE;
INSERT INTO `Login` VALUES (1, '2021-10-24-10-28-36');
INSERT INTO `Login` VALUES (2, '2021-10-24-12-10-54');
INSERT INTO `Login` VALUES (3, '2021-10-24-15-47-02');
INSERT INTO `Login` VALUES (4, '2021-10-24-16-03-21');
INSERT INTO `Login` VALUES (5, '2021-10-24-20-58-33');
INSERT INTO `Login` VALUES (3, '2021-10-25-09-15-27');
INSERT INTO `Login` VALUES (2, '2021-10-27-22-52-51');
INSERT INTO `Login` VALUES (5, '2021-10-28-19-43-09');
UNLOCK TABLES;

CREATE TABLE `Account` (
  `user_id` int NOT NULL,
  `account_id` int NOT NULL,
  `type` varchar(10) NOT NULL,
  `balance` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Account` WRITE;
INSERT INTO `Account` VALUES (1, 1, 'HKD', 550);
INSERT INTO `Account` VALUES (2, 1, 'HKD', 2500);
INSERT INTO `Account` VALUES (3, 1, 'USD', 800);
INSERT INTO `Account` VALUES (3, 2, 'HKD', 1600);
INSERT INTO `Account` VALUES (4, 1, 'HKD', 5200);
INSERT INTO `Account` VALUES (5, 1, 'HKD', 100000);
INSERT INTO `Account` VALUES (5, 2, 'USD', 50000);
INSERT INTO `Account` VALUES (5, 3, 'RMB', 1000000000);
UNLOCK TABLES;

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
INSERT INTO `Transaction` VALUES (1, 4, 1, 1, 1, 'HKD', 200, '2021-10-24-16-05-33');
INSERT INTO `Transaction` VALUES (2, 5, 3, 1, 2, 'HKD', 1000, '2021-10-24-21-00-04');
INSERT INTO `Transaction` VALUES (3, 2, 1, 1, 1, 'HKD', 50, '2021-10-27-22-52-51');
UNLOCK TABLES;

CREATE TABLE `Friend` (
  `user_id1` int NOT NULL,
  `user_id2` int NOT NULL,
  `established_time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Friend` WRITE;
INSERT INTO `Friend` VALUES (1, 5, '2021-10-24');
INSERT INTO `Friend` VALUES (2, 3, '2021-10-24');
INSERT INTO `Friend` VALUES (2, 4, '2021-10-24');
INSERT INTO `Friend` VALUES (1, 3, '2021-10-25');
UNLOCK TABLES;

