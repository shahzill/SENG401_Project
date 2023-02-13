DROP DATABASE IF EXISTS STUDENTHUB;
CREATE DATABASE STUDENTHUB; 
USE STUDENTHUB;

DROP TABLE IF EXISTS `registered-users`;
 
CREATE TABLE `registered-users` (
  `email` varchar(45) NOT NULL,
  `ucid` int NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` char(40) NOT NULL,
  PRIMARY KEY (`email`,`ucid`)
);