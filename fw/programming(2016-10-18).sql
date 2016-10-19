-- phpMyAdmin SQL Dump
-- version 4.6.4deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2016-10-18 16:20:39
-- 服务器版本： 5.6.30-1
-- PHP Version: 7.0.10-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `programming`
--
CREATE DATABASE IF NOT EXISTS `programming` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `programming`;

DELIMITER $$
--
-- 存储过程
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc1` (OUT `s` INT)  BEGIN
SELECT COUNT(*) INTO s FROM `prog_info`;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `proc2` (OUT `s` INT)  BEGIN
SELECT * FROM `prog_info`;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `proc3` (IN `cu` VARCHAR(30))  NO SQL
BEGIN
SELECT * FROM programming.prog_info WHERE customer = cu;
END$$

CREATE DEFINER=`prog`@`%` PROCEDURE `ups_new_fw_available` (IN `customer` VARCHAR(30), IN `model` VARCHAR(30), IN `component_designator` VARCHAR(10), OUT `v_fw_version` VARCHAR(30), OUT `v_fw_checksum` VARCHAR(30), OUT `v_fw_pathname` VARCHAR(100))  BEGIN
SELECT `fw_version`, `fw_checksum`, `fw_pathname` INTO v_fw_version, v_fw_checksum, v_fw_pathname 
FROM `prog_info` 
WHERE `prog_info`.`customer`= customer 
    AND `prog_info`.`model`= model 
    AND `prog_info`.`component_designator`= component_designator
ORDER BY `id` DESC LIMIT 1
   ;
-- SELECT v_fw_version AS fw_version, v_fw_checksum AS fw_checksum;--
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- 表的结构 `prog_info`
--

CREATE TABLE `prog_info` (
  `id` bigint(20) NOT NULL,
  `customer` varchar(30) NOT NULL,
  `model` varchar(30) NOT NULL,
  `pn` varchar(30) NOT NULL,
  `component_designator` varchar(10) NOT NULL,
  `mcu_model` varchar(30) NOT NULL,
  `fw_pathname` varchar(300) NOT NULL,
  `fw_version` varchar(30) NOT NULL,
  `fw_checksum` varchar(30) NOT NULL,
  `dl_port` varchar(30) NOT NULL,
  `dl_speed` varchar(30) NOT NULL,
  `flash_start_addr` varchar(30) NOT NULL,
  `flash_length` varchar(30) NOT NULL,
  `sn_enable` tinyint(1) NOT NULL,
  `sn_addr` varchar(30) DEFAULT NULL,
  `sn_length` varchar(30) DEFAULT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `prog_info`
--

INSERT INTO `prog_info` (`id`, `customer`, `model`, `pn`, `component_designator`, `mcu_model`, `fw_pathname`, `fw_version`, `fw_checksum`, `dl_port`, `dl_speed`, `flash_start_addr`, `flash_length`, `sn_enable`, `sn_addr`, `sn_length`, `datetime`) VALUES
(1, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14595', '0x11223344', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-09-30 09:00:00'),
(2, 'vivint', 'v-mp2-345', 'v-mp2-345', 'U13', 'SanDisk8G', '/prog/image.bin', '12345', '0x1020304050', 'JTAG', '4000 kHz', '0x400000', '8G', 0, NULL, NULL, '2016-10-11 09:00:00'),
(3, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14721', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00'),
(4, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14722', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00'),
(5, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14723', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00'),
(6, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14724', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00'),
(7, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14725', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00'),
(8, '2GIG', '2GIG-RELY-345', '2GIG-RELY-345', 'U4', 'ATSAM4SD32C', '/prog/2BIT_PANEL.bin', '14726', '0X6E683164', 'JTAG', '4000 kHz', '0x400000', '2048 KB', 0, NULL, NULL, '2016-10-13 15:00:00');

-- --------------------------------------------------------

--
-- 表的结构 `tb1`
--

CREATE TABLE `tb1` (
  `id` int(11) NOT NULL,
  `name` int(11) NOT NULL,
  `sex` int(11) NOT NULL,
  `ppp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `prog_info`
--
ALTER TABLE `prog_info`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `prog_info`
--
ALTER TABLE `prog_info`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
