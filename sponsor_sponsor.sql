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
-- Table structure for table `sponsor_sponsor`
--

DROP TABLE IF EXISTS `sponsor_sponsor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sponsor_sponsor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `logo` varchar(500) NOT NULL,
  `sponsor_name` varchar(500) NOT NULL,
  `status` int NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `website_url` varchar(500) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sponsor_sponsor`
--

LOCK TABLES `sponsor_sponsor` WRITE;
/*!40000 ALTER TABLE `sponsor_sponsor` DISABLE KEYS */;
INSERT INTO `sponsor_sponsor` VALUES (7,'2023-05-06 06:11:14.645259','sponsor/AI4D_L.jpg','The Artificial Intelligence for Development in Africa ',1,'2023-05-06 06:11:14.645266','https://www.acts-net.org/ai4d-africa','<p>AI4D Africa is a 3-year project, funded by the International Development Research Centre (IDRC) and the Swedish International Development Cooperation Agency (Sida)</p>\r\n'),(8,'2023-05-06 06:15:19.157124','sponsor/crdi_L.jpg','The International Development Research Centre (IDRC) ',1,'2023-05-06 06:15:19.157131','https://www.idrc.ca/en','<p>As part of Canada&rsquo;s foreign affairs and development efforts, the International Development Research Centre (IDRC) champions and funds research and innovation within and alongside developing regions to drive global change</p>\r\n'),(9,'2023-05-06 06:18:12.286739','sponsor/sida_L.jpg','The Swidish International Development Cooparation Agency',1,'2023-05-06 06:18:12.286752','https://www.sida.se/en/','<p>Sida is Sweden&#39;s government agency for development cooperation. We strive to reduce poverty and oppression around the world.</p>\r\n');
/*!40000 ALTER TABLE `sponsor_sponsor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-08 17:05:13
