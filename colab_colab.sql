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
-- Table structure for table `colab_colab`
--

DROP TABLE IF EXISTS `colab_colab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colab_colab` (
  `id` int NOT NULL AUTO_INCREMENT,
  `colab_name` varchar(500) NOT NULL,
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
-- Dumping data for table `colab_colab`
--

LOCK TABLES `colab_colab` WRITE;
/*!40000 ALTER TABLE `colab_colab` DISABLE KEYS */;
INSERT INTO `colab_colab` VALUES (7,'The Council for Scientific and Industrial Research (CSIR) ','colab/csir_L.jpg',1,'2023-05-06 06:20:51.314671','2023-05-06 06:20:51.314681','https://www.csir.co.za/','<p>The Council for Scientific and Industrial Research (CSIR) is a leading scientific and technology research organisation that researches, develops, localises and diffuses technologies to accelerate socioeconomic prosperity in South Africa.</p>\r\n'),(8,'Ifakara Health Institute','colab/ihi_L.jpg',1,'2023-05-06 06:23:01.804488','2023-05-06 06:23:01.804512','https://ihi.or.tz/','<p>Ifakara Health Institute (IHI) is a leading health research organization in Africa, with a strong track record of developing, testing and validating innovations for health. We are driven by core strategic mandate for research, training and services.</p>\r\n'),(9,'Tanzania Data Lab','colab/dlab_L.jpg',1,'2023-05-06 06:24:16.163550','2023-05-06 06:24:16.163585','https://dlab.or.tz/','<p>Tanzania Data Lab (dLab) is a world class data and innovation lab that harnesses the potential of the data revolution and the fourth industrial revolution in solving local, regional, and global sustainable development challenges through data and innovation.</p>\r\n');
/*!40000 ALTER TABLE `colab_colab` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-08 17:04:03
