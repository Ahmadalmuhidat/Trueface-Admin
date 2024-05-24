-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: TimeWizeAI
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Attendance`
--

DROP TABLE IF EXISTS `Attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Attendance` (
  `AttendanceID` varchar(200) DEFAULT NULL,
  `AttendanceStudentID` varchar(200) DEFAULT NULL,
  `AttendanceClassID` varchar(200) DEFAULT NULL,
  `AttendanceTime` time DEFAULT NULL,
  `AttendanceDate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Attendance`
--

LOCK TABLES `Attendance` WRITE;
/*!40000 ALTER TABLE `Attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `Attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Classes`
--

DROP TABLE IF EXISTS `Classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Classes` (
  `ClasseID` varchar(200) DEFAULT NULL,
  `ClassSubjectArea` varchar(200) DEFAULT NULL,
  `ClasseCatalogNBR` int DEFAULT NULL,
  `ClasseAcademicCareer` varchar(200) DEFAULT NULL,
  `ClasseCourseID` varchar(200) DEFAULT NULL,
  `ClasseCourseOfferingNBR` int DEFAULT NULL,
  `ClasseSessionStartTime` time DEFAULT NULL,
  `ClasseSessionEndTime` time DEFAULT NULL,
  `ClasseSection` varchar(200) DEFAULT NULL,
  `ClasseComponent` varchar(200) DEFAULT NULL,
  `ClasseCampus` varchar(200) DEFAULT NULL,
  `ClasseInstructorID` varchar(200) DEFAULT NULL,
  `ClasseInstructorType` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Classes`
--

LOCK TABLES `Classes` WRITE;
/*!40000 ALTER TABLE `Classes` DISABLE KEYS */;
INSERT INTO `Classes` VALUES ('1','ll',77,'jj','fff',7,'00:00:07','00:00:07','jj','j','jj','jj','jj');
/*!40000 ALTER TABLE `Classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Courses` (
  `CourseID` varchar(200) DEFAULT NULL,
  `CourseTitle` varchar(200) DEFAULT NULL,
  `CourseCredit` int DEFAULT NULL,
  `CourseMaximumUnits` int DEFAULT NULL,
  `CourseLongCourseTitle` varchar(200) DEFAULT NULL,
  `CourseOfferingNBR` int DEFAULT NULL,
  `CourseAcademicGroup` varchar(200) DEFAULT NULL,
  `CourseSubjectArea` varchar(200) DEFAULT NULL,
  `CourseCatalogNBR` int DEFAULT NULL,
  `CourseCampus` varchar(200) DEFAULT NULL,
  `CourseAcademicOrganization` varchar(200) DEFAULT NULL,
  `CourseComponent` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Courses`
--

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Courses` DISABLE KEYS */;
INSERT INTO `Courses` VALUES ('fff','ff',44,44,'ff',44,'ff','ff',44,'ff','ff','ff'),('43','ddd',44,44,'ddd',44,'dd','dd',444,'ddd','dd','dd'),('66','nnn',999,999,'nnn',99,'nn','nn',99,'rr','rr','rr');
/*!40000 ALTER TABLE `Courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Instructors`
--

DROP TABLE IF EXISTS `Instructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Instructors` (
  `InstructorID` varchar(200) DEFAULT NULL,
  `InstructorFirstName` varchar(200) DEFAULT NULL,
  `InstructorMiddleName` varchar(200) DEFAULT NULL,
  `InstructorLastName` varchar(200) DEFAULT NULL,
  `InstructorEmail` varchar(200) DEFAULT NULL,
  `InstructorPass` varchar(200) DEFAULT NULL,
  `InstructorCreateDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Instructors`
--

LOCK TABLES `Instructors` WRITE;
/*!40000 ALTER TABLE `Instructors` DISABLE KEYS */;
/*!40000 ALTER TABLE `Instructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Licenses`
--

DROP TABLE IF EXISTS `Licenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Licenses` (
  `LicenseID` varchar(200) DEFAULT NULL,
  `LicenseActivationKey` varchar(200) DEFAULT NULL,
  `LicenseCustomer` varchar(200) DEFAULT NULL,
  `LicenseStartDate` datetime DEFAULT NULL,
  `LicenseEndDate` datetime DEFAULT NULL,
  `LicenseActive` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Licenses`
--

LOCK TABLES `Licenses` WRITE;
/*!40000 ALTER TABLE `Licenses` DISABLE KEYS */;
INSERT INTO `Licenses` VALUES ('1','1234','KAUST','2000-01-01 00:00:00','2030-01-01 00:00:00',1);
/*!40000 ALTER TABLE `Licenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `StudentID` varchar(200) DEFAULT NULL,
  `StudentFirstName` varchar(200) DEFAULT NULL,
  `StudentMiddleName` varchar(200) DEFAULT NULL,
  `StudentLastName` varchar(200) DEFAULT NULL,
  `StudentGender` varchar(200) DEFAULT NULL,
  `StudentFaceID` blob,
  `StudentCreatedate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-24 13:12:50
