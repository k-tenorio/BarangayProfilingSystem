-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2026 at 04:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `barangay_profiling`
--

-- --------------------------------------------------------

--
-- Table structure for table `residents`
--

CREATE TABLE `residents` (
  `resident_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `sex` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  `place_of_birth` varchar(100) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `religion` varchar(50) DEFAULT NULL,
  `civil_status` enum('Single','Married','Widowed','Separated') NOT NULL,
  `is_deceased` tinyint(1) DEFAULT 0,
  `is_pwd` tinyint(1) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_archived` tinyint(1) DEFAULT 0,
  `archived_at` datetime DEFAULT NULL,
  `archived_by` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `residents`
--

INSERT INTO `residents` (`resident_id`, `first_name`, `middle_name`, `last_name`, `sex`, `date_of_birth`, `place_of_birth`, `nationality`, `religion`, `civil_status`, `is_deceased`, `is_pwd`, `created_at`, `updated_at`, `is_archived`, `archived_at`, `archived_by`) VALUES
(2, 'Aasdas', 'A', 'Aada', 'Male', '1950-01-01', 'A', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:29:41', '2026-04-13 23:27:44', 0, NULL, NULL),
(3, 'B', 'B', 'B', 'Male', '2000-02-19', 'B', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:30:38', '2026-02-19 12:30:38', 0, NULL, NULL),
(4, 'C', 'C', 'C', 'Male', '2015-02-19', 'C', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:31:21', '2026-02-19 12:31:21', 0, NULL, NULL),
(5, 'D', 'D', 'D', 'Male', '1999-02-19', 'D', 'Filipino', 'Born Again', 'Married', 0, 0, '2026-02-19 12:31:55', '2026-02-19 12:31:55', 0, NULL, NULL),
(6, 'E', 'E', 'E', 'Male', '2006-03-15', 'E', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:32:27', '2026-02-19 12:32:27', 0, NULL, NULL),
(7, 'F', 'F', 'F', 'Male', '2000-01-01', 'F', 'Filipino', 'Inglesia ni Cristo', 'Single', 0, 0, '2026-02-19 12:34:10', '2026-02-19 12:34:10', 0, NULL, NULL),
(8, 'G', 'G', 'G', 'Male', '2016-02-11', 'G', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:34:50', '2026-03-01 12:15:22', 0, NULL, NULL),
(10, 'I', 'I', 'I', 'Male', '1969-02-19', 'I', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-02-19 12:36:26', '2026-02-19 12:36:26', 0, NULL, NULL),
(11, 'J', 'J', 'J', 'Male', '1967-02-19', 'J', 'Filipino', 'Roman Catholic', 'Single', 0, 1, '2026-02-19 12:37:15', '2026-02-19 12:37:15', 0, NULL, NULL),
(14, 'K', 'K', 'K', 'Male', '2006-03-15', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-03-03 15:39:45', '2026-03-03 15:39:45', 0, NULL, NULL),
(15, 'test1', '', 'test1', 'Male', '2000-01-01', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-03-03 16:08:44', '2026-04-10 17:20:04', 0, NULL, NULL),
(16, 'test', '', 'staff', 'Male', '2000-01-01', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-03-16 00:39:25', '2026-03-26 12:51:01', 0, NULL, NULL),
(17, 'test 2', '', 'test 2', 'Female', '2000-01-01', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-03-16 00:40:49', '2026-03-26 12:50:47', 0, NULL, NULL),
(25, 'LAST', 'LAST', 'LAST', 'Male', '2003-01-04', 'wqqewq', 'American', 'Born Again', 'Married', 0, 0, '2026-04-07 12:44:18', '2026-04-07 12:49:05', 0, NULL, NULL),
(26, 'TEST FINAL', 'TEST FINALasdsadas', 'TEST FINALdsadsadsa', 'Female', '1999-01-01', 'test', 'Filipino', 'Roman Catholic', 'Separated', 0, 0, '2026-04-10 11:06:42', '2026-04-10 11:09:25', 0, NULL, NULL),
(27, 'VERY', '', 'TTT', 'Male', '2000-01-01', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 1, '2026-04-10 14:35:26', '2026-04-10 14:36:08', 0, NULL, NULL),
(28, 'Kobe', '', 'Tenorio', 'Male', '2000-01-01', 'test', 'Filipino', 'Roman Catholic', 'Single', 0, 0, '2026-04-10 17:42:22', '2026-04-14 00:13:29', 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `resident_addresses`
--

CREATE TABLE `resident_addresses` (
  `address_id` int(11) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `purok` varchar(50) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `house_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_addresses`
--

INSERT INTO `resident_addresses` (`address_id`, `resident_id`, `purok`, `street`, `house_id`) VALUES
(3, 2, 'Purok 1', 'A', '1'),
(4, 3, 'Purok 1', 'B', '2'),
(5, 4, 'Purok 1', 'C', '3'),
(6, 5, 'Purok 1', 'D', '4'),
(7, 6, 'Purok 1', 'E', '5'),
(9, 7, 'Purok 2', 'F', '6'),
(10, 8, 'Purok 1', 'G', '7'),
(12, 10, 'Purok 4', 'I', '9'),
(13, 11, 'Purok 5', 'J', '10'),
(23, 14, 'Purok 5', 'Talomo Cemento', '1'),
(24, 15, 'Purok 1', 'test', '123'),
(27, 16, 'Purok 5', 'test', '21'),
(28, 17, 'Purok 1', 'test', '21'),
(47, 25, 'Purok 4', '21332', '312'),
(49, 26, 'Purok 2', 'dadsadsa', '12321'),
(52, 27, 'Purok 4', 'test', '123'),
(54, 28, 'Purok 1', 'test', '13213');

-- --------------------------------------------------------

--
-- Table structure for table `resident_contacts`
--

CREATE TABLE `resident_contacts` (
  `contact_id` int(11) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_contacts`
--

INSERT INTO `resident_contacts` (`contact_id`, `resident_id`, `contact_number`, `email`) VALUES
(3, 2, '1111111111', 'A@.'),
(4, 3, '1111111111', 'B@.'),
(5, 4, '1111111111', 'C@.'),
(6, 5, '1111111111', 'D@.'),
(7, 6, '1111111111', 'E@.'),
(9, 7, '1111111111', 'F@.'),
(10, 8, '1111111111', 'G@.'),
(12, 10, '1111111111', 'I@.'),
(13, 11, '1111111111', 'J@.'),
(23, 14, '00000000000', '@.'),
(24, 15, '0000000000', '@.'),
(27, 16, '123123123', '@.'),
(28, 17, '123123123', '@.'),
(47, 25, '1231312', '@.'),
(49, 26, '1232132', '@dasda.'),
(52, 27, '31312312', '@.'),
(54, 28, '12321321', '@.');

-- --------------------------------------------------------

--
-- Table structure for table `resident_emergency_contacts`
--

CREATE TABLE `resident_emergency_contacts` (
  `emergency_id` int(11) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `emergency_contact_name` varchar(100) DEFAULT NULL,
  `emergency_contact_number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_emergency_contacts`
--

INSERT INTO `resident_emergency_contacts` (`emergency_id`, `resident_id`, `emergency_contact_name`, `emergency_contact_number`) VALUES
(3, 2, 'A', '1111111111'),
(4, 3, 'B', '1111111111'),
(5, 4, 'C', '1111111111'),
(6, 5, 'D', '1111111111'),
(7, 6, 'E', '1111111111'),
(9, 7, 'F', '1111111111'),
(10, 8, 'G', '1111111111'),
(12, 10, 'I', '1111111111'),
(13, 11, 'J', '1111111111'),
(23, 14, 'test', '0000000000'),
(24, 15, 'test', '0000000000'),
(27, 16, 'test', '123123123'),
(28, 17, 'test', '123123123'),
(47, 25, 'Sdkadk21321', '13231231'),
(49, 26, 'sadsad', '23121321'),
(52, 27, 'test', '1231321'),
(54, 28, 'test', '132321213213');

-- --------------------------------------------------------

--
-- Table structure for table `resident_parents`
--

CREATE TABLE `resident_parents` (
  `parent_id` int(11) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `mother_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_parents`
--

INSERT INTO `resident_parents` (`parent_id`, `resident_id`, `father_name`, `mother_name`) VALUES
(3, 2, 'A', 'A'),
(4, 3, 'B', 'B'),
(5, 4, 'C', 'C'),
(6, 5, 'D', 'D'),
(7, 6, 'E', 'E'),
(9, 7, 'F', 'F'),
(10, 8, 'G', 'G'),
(12, 10, 'I', 'I'),
(13, 11, 'J', 'J'),
(23, 14, 'test', 'test'),
(24, 15, 'testte', 'test'),
(27, 16, 'test', 'test'),
(28, 17, 'test', 'test'),
(47, 25, 'adpadsa', 'sdasdad'),
(49, 26, 'fsdfds', 'dafafds'),
(52, 27, 'test', 'test'),
(54, 28, 'test', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `resident_physical_info`
--

CREATE TABLE `resident_physical_info` (
  `physical_id` int(11) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `blood_type` varchar(5) DEFAULT NULL,
  `height_cm` decimal(5,2) DEFAULT NULL,
  `weight_kg` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_physical_info`
--

INSERT INTO `resident_physical_info` (`physical_id`, `resident_id`, `blood_type`, `height_cm`, `weight_kg`) VALUES
(3, 2, 'A+', 150.00, 80.00),
(4, 3, 'A+', 150.00, 80.00),
(5, 4, 'B-', 150.00, 80.00),
(6, 5, 'O+', 150.00, 80.00),
(7, 6, 'AB-', 180.00, 80.00),
(9, 7, 'O+', 150.00, 80.00),
(10, 8, 'A+', 150.00, 80.00),
(12, 10, 'A+', 150.00, 80.00),
(13, 11, 'A+', 150.00, 50.00),
(23, 14, 'A+', 180.00, 80.00),
(24, 15, 'A+', 180.00, 50.00),
(27, 16, 'A+', 123.00, 123.00),
(28, 17, 'A+', 123.00, 123.00),
(47, 25, 'A+', 123.00, 131.00),
(49, 26, 'B+', 213.00, 123.00),
(52, 27, 'A+', 123.00, 132.00),
(54, 28, 'O-', 132.00, 123.00);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('Secretary','Staff') NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `role`, `full_name`, `contact_number`, `email`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'secretary1', '$2b$12$d4m54eomxuJRKpwp4/bSWubERkFJ34luI0esKMah/GzDpy/OYFOMG', 'Secretary', 'test1 test1', NULL, NULL, 1, '2026-01-30 22:40:52', '2026-03-16 20:22:43'),
(3, 'staff1', '$2b$12$SHqMRAFKTlN50zFuDnbV7OQeyS3WpxH7Pn/jEPphab8OTwzr4hur6', 'Staff', 'test3 test3', NULL, NULL, 1, '2026-01-30 22:43:05', '2026-03-16 20:22:43'),
(4, 'staff2', '$2b$12$QHBbGNf4m76XE/mveGGk0.xqs6KO0eOKE43XIQOBE8afs40JSKWEu', 'Staff', 'test3 test3', NULL, NULL, 1, '2026-01-30 22:43:09', '2026-03-16 20:22:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `residents`
--
ALTER TABLE `residents`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `idx_is_archived` (`is_archived`);

--
-- Indexes for table `resident_addresses`
--
ALTER TABLE `resident_addresses`
  ADD PRIMARY KEY (`address_id`),
  ADD UNIQUE KEY `resident_id` (`resident_id`);

--
-- Indexes for table `resident_contacts`
--
ALTER TABLE `resident_contacts`
  ADD PRIMARY KEY (`contact_id`),
  ADD UNIQUE KEY `resident_id` (`resident_id`);

--
-- Indexes for table `resident_emergency_contacts`
--
ALTER TABLE `resident_emergency_contacts`
  ADD PRIMARY KEY (`emergency_id`),
  ADD UNIQUE KEY `resident_id` (`resident_id`);

--
-- Indexes for table `resident_parents`
--
ALTER TABLE `resident_parents`
  ADD PRIMARY KEY (`parent_id`),
  ADD UNIQUE KEY `resident_id` (`resident_id`);

--
-- Indexes for table `resident_physical_info`
--
ALTER TABLE `resident_physical_info`
  ADD PRIMARY KEY (`physical_id`),
  ADD UNIQUE KEY `resident_id` (`resident_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `residents`
--
ALTER TABLE `residents`
  MODIFY `resident_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `resident_addresses`
--
ALTER TABLE `resident_addresses`
  MODIFY `address_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `resident_contacts`
--
ALTER TABLE `resident_contacts`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `resident_emergency_contacts`
--
ALTER TABLE `resident_emergency_contacts`
  MODIFY `emergency_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `resident_parents`
--
ALTER TABLE `resident_parents`
  MODIFY `parent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `resident_physical_info`
--
ALTER TABLE `resident_physical_info`
  MODIFY `physical_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `resident_addresses`
--
ALTER TABLE `resident_addresses`
  ADD CONSTRAINT `resident_addresses_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `residents` (`resident_id`) ON DELETE CASCADE;

--
-- Constraints for table `resident_contacts`
--
ALTER TABLE `resident_contacts`
  ADD CONSTRAINT `resident_contacts_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `residents` (`resident_id`) ON DELETE CASCADE;

--
-- Constraints for table `resident_emergency_contacts`
--
ALTER TABLE `resident_emergency_contacts`
  ADD CONSTRAINT `resident_emergency_contacts_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `residents` (`resident_id`) ON DELETE CASCADE;

--
-- Constraints for table `resident_parents`
--
ALTER TABLE `resident_parents`
  ADD CONSTRAINT `resident_parents_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `residents` (`resident_id`) ON DELETE CASCADE;

--
-- Constraints for table `resident_physical_info`
--
ALTER TABLE `resident_physical_info`
  ADD CONSTRAINT `resident_physical_info_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `residents` (`resident_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
