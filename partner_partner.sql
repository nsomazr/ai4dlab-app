-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: containers-us-west-94.railway.app    Database: railway
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `partner_partner`
--

DROP TABLE IF EXISTS `partner_partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partner_partner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `partner_name` varchar(500) NOT NULL,
  `logo` varchar(500) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `website_url` varchar(500) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partner_partner`
--

LOCK TABLES `partner_partner` WRITE;
/*!40000 ALTER TABLE `partner_partner` DISABLE KEYS */;
INSERT INTO `partner_partner` VALUES (8,'The University of Dodoma','partner/udom_L_ULeeLJi.jpg',1,'2023-04-06 10:12:21.716511','2023-04-06 10:12:21.716533','https://udom.ac.tz','<p>The University of Dodoma (<strong>UDOM</strong>) is a public university in central Tanzania located in Dodoma.</p>\r\n'),(9,'The Nelson Mandela African Institution of Science and Technology','partner/nelson_L_9HVHGin.jpg',1,'2023-04-06 10:16:02.724300','2023-04-06 10:16:02.724308','https://nm-aist.ac.tz','<p>The Nelson Mandela African Institution of Science and Technology in Arusha (<strong>NM-AIST Arusha</strong>) is part of the network of Pan-African Institutes of Science and Technology located across the continent.</p>\r\n');
/*!40000 ALTER TABLE `partner_partner` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-08 17:07:54
