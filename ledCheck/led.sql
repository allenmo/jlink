-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2016 年 11 月 02 日 17:16
-- 服务器版本: 5.5.36
-- PHP 版本: 5.3.28

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `led`
--

-- --------------------------------------------------------

--
-- 表的结构 `check_led`
--

CREATE TABLE IF NOT EXISTS `check_led` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `x` int(11) DEFAULT NULL,
  `y` int(11) DEFAULT NULL,
  `R1` int(11) DEFAULT NULL,
  `R2` int(11) DEFAULT NULL,
  `L1` int(11) DEFAULT NULL,
  `U1` int(11) DEFAULT NULL,
  `L2` int(11) DEFAULT NULL,
  `U2` int(11) DEFAULT NULL,
  `L3` int(11) DEFAULT NULL,
  `U3` int(11) DEFAULT NULL,
  `color_space` enum('RGB','HSV','HSL') NOT NULL COMMENT 'RGB, HSV, HSL',
  `mode` enum('CIRCLE','RING','RECTANGLE') NOT NULL COMMENT 'circle, ring',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
