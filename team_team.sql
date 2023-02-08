-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: ai4dlabdb
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

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
-- Table structure for table `team_team`
--

DROP TABLE IF EXISTS `team_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team_team` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `bio` longtext NOT NULL,
  `linkedin_url` varchar(200) DEFAULT NULL,
  `twitter_url` varchar(200) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `photo` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `affiliation` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_team`
--

LOCK TABLES `team_team` WRITE;
/*!40000 ALTER TABLE `team_team` DISABLE KEYS */;
INSERT INTO `team_team` VALUES (4,'Dr. Ally','Nyamawe','Principal Investigator (PI)','Ally S. Nyamawe, is a Lecturer of Computer Science at the University of Dodoma, Tanzania. He obtained MSc in Computer Science from the University of Dodoma, and a Ph.D. degree in Computer Science and Technology from the Beijing Institute of Technology, China. Nyamawe has significant research experience in the application of Artificial Intelligence (AI) in Software engineering. \r\n\r\nHis research interests include Software Engineering, Machine Learning, and AI for Social Good (AI4SG). He served on the program committees for prestigious conferences including the 37 th IEEE/ACM International Conference on Automated Software Engineering. Since 2009, Nyamawe has served the University of Dodoma in a different capacity. From 2013 to 2015, he served as the Head of the Department of Computer science. \r\n\r\nHe was a Coordinator of the then Center for Innovation, Research, and Development in ICT of the College of Informatics and Virtual Education. Prior to that, Nyamawe served St. John’s University of Tanzania as Software Developer and Instructor from 2008 to 2009. Nyamawe is also currently serving as a Manager of Africa’s Anglophone Artificial Intelligence for Development (AI4D) Multidisciplinary Research Lab. With the lab, Nyamawe is working towards accelerating AI uptake for sustainable development in Africa. He is an AI4SG strategist and advocates explainable, inclusive, and responsible AI','https://www.linkedin.com/in/ally-nyamawe-55781058/','https://twitter.com/allynyamawe','255715016580','ally.nyamawe@ai4dlab.or.tz',1,'team/Mr_Nyamawe.jpg','2023-02-08 14:29:36.389745','2023-02-08 14:29:36.389755','The University of Dodoma'),(5,'Prof. Shubi','Kaijage','Co-Principal Investigator (Co-PI)','None','https://linkedin.com/in/shubif','https://twitter.com/ShubiF','0','shubi.kaijage@ai4dlab.or.tz',1,'team/Prof_Shubi.jpg','2023-02-08 15:10:30.731342','2023-02-08 15:10:30.731356','Nelson Mandela African Institute of Science and Technology'),(6,'Dr. Mohamedi','M. Mjahidi','Lab and Training Coordinator','Mohamedi M. Mjahidi is a Lecturer and researcher at the Department of Computer Science and Engineering (DoCSE), College of Informatics and Virtual Education (CIVE), the University of Dodoma (UDOM), Tanzania. He graduated from the University of Dar es Salaam (UDSM) in 2006 with BSc. in Computer Science and completed his MSc. in Telecommunications Engineering at the University of Dodoma in 2011. \r\n\r\nHe then pursued his Ph.D. in Computer Engineering at the Gazi University, Ankara, Turkey in 2020. His research interest includes computer and mobile networking, Artificial Intelligence and Machine Learning. Mjahidi served as the Head of the Department of Computer Applications and Technologies (DoCAT) from 2012 to 2013.','https://www.linkedin.com/in/mohamedi-mjahidi-528ab7139/','https://twitter.com/mmjahidi','255778975083','mohamedi.mjahidi@ai4dlab.or.tz',1,'team/Mr_Mjahidi.jpg','2023-02-08 15:14:40.068963','2023-02-08 15:14:40.068979','The University of Dodoma'),(7,'Ms. Gloriana','Monko','Liaison Officer','Gloriana J. Monko is an Assistant Lecturer, AI enthusiast and a researcher at the Department of Computer Science and Engineering at the College of Informatics and Virtual Education- UDOM. She is also taking her PhD studies in Natural Language Processing at Shibaura Institute of Technology, Tokyo. \r\n\r\nShe has fairly an experience on research projects and consultancies around the area of her expertise and her research interests focus on: Computer Science, Machine Learning, Natural Language Processing; STEM initiatives, Promoting Gender equality and inclusion; Critical thinking and Problem solving for employability and social change.','https://www.linkedin.com/in/gloriana-monko-b83368121/','https://twitter.com/GlorianaMonko','0','gloriana.monko@ai4dlab.or.tz',1,'team/Ms_Gloriana.jpg','2023-02-08 15:17:48.725692','2023-02-08 15:17:48.725717','The University of Dodoma'),(8,'Mr. Salim','Diwani','Coordinator - Healthcare','Salim Diwani is an Academic staff in the Department of Computer Science and Engineering at the University of Dodoma, with over 12 years of experience in academic and research. He received his BS and M.Sc. degrees in Computer Science from Jamia Hamdard University, New Delhi, India in 2006 and in 2008. His research interests focus on developing novel data analytics and machine learning techniques, especially for applications in text mining, social network analysis, and biomedical informatics. \r\n\r\nDiwani is passionate about developing young talents to achieve their goals and see them grow in their careers, supervising BSc students and mentoring them. Diwani has recently also become interested in AI ethics, policies and strategies in developing countries like Tanzania, not because he has any answers but has lots of questions for AI implementation in Africa. Diwani is also currently serving as a Healthcare Coordinator of Africa\'s Anglophone Artificial Intelligence for Development (AI4D) Multidisciplinary Research Lab Project. For more information about Diwani\'s publications, visit his Google scholar page at https://scholar.google.com/citations?user=ai1c-coAAAAJ&hl=en','None','None','0','salim.diwani@ai4dlab.or.tz',1,'team/Dr_Diwani.jpg','2023-02-08 15:21:03.854843','2023-02-08 15:21:03.854852','The University of Dodoma'),(9,'Dr. Devotha','Nyambo','Coordinator - Environment Conservation and Agriculture','Devotha Godfrey Nyambo is a researcher and lecturer at the Nelson Mandela African Institution of Science and Technology, Tanzania. She has a PhD in Information and Communication Sciences and Engineering from the Nelson Mandela African Institution of Science and Technology (2020). Her research focus has been on Artificial Intelligence (AI) and modeling of agricultural systems, especially livestock systems. \r\n\r\nShe leads the Artificial Intelligence and Complexity Sciences research group at the institution and also leads the Agriculture and Environmental Conservation group at Africa\'s Anglophone Artificial Intelligence for Development (AI4D) Multidisciplinary Research Lab. Her current project is on Leveraging Multi-Agent Models for Learning Recommendations and Improvement of Farmer-to-Farmer Interactions in Small Scale Dairy. \r\n\r\nHer research interests extend to the application of AI in the health and education sectors. Devotha is a member of the African Women in Agricultural Research and Development (AWARD) and also, the Organization for Women in Science for the Developing World (OWSD).','None','None','255752905156','devotha.nyambo@ai4dlab.or.tz',1,'team/Dr_Devota.jpg','2023-02-08 15:24:35.423718','2023-02-08 15:24:35.423752','Nelson Mandela African Institute of Science and Technology'),(10,'Dr. Jabhera Maseke','Matogoro','Coordinator - Infrastructure and Data Ecosystem','Jabhera Matogoro holds PhD in Telecommunications Engineering and MSc. in Computer Science from the University of Dodoma. Dr. Matogoro received his Bachelor of Science in Computer Science from University of Dar es Salaam. Dr Matogoro is working as a Lecturer in the Department of Computer Science and Engineering of the College of Informatics and Virtual Education. \r\n\r\nDr Matogoro is an Open Internet Engineering Mozilla Fellow for the year 2019 – 2020 and The Centre for Science and Technology of the Non-Aligned and Other Developing Countries (NAM S&T Centre) Fellow to Indian Institute of Technology Bombay in 2015/16, Mumbai, India. Jabhera Matogoro is working to scale-up community-owned cooperative societies in Tanzania aimed at making cooperative attractive for youth and young girls in Tanzania, while at the same time addressing challenges associated with broadband Internet access.','https://www.linkedin.com/in/dr-jabhera-matogoro-02541518/','https://twitter.com/jaberamatogoro','255784423615','jabhera.matogoro@ai4dlab.or.tz',1,'team/Matogoro.jpg','2023-02-08 15:27:39.081029','2023-02-08 15:27:39.081050','The University of Dodoma'),(12,'Dr. Neema','Mduma','Assistant Coordinator for Environmental Conservation and Agriculture','Dr. Neema Mduma is a computer scientist and a lecturer in the school of Computational and Communication Sciences and Engineering (CoCSE) at the Nelson Mandela African Institution of Science and Technology (NM-AIST). She obtained her Ph.D. in Information and Communication Sciences and Engineering from the Nelson Mandela African Institution of Science and Technology (NM-AIST). \r\n\r\nNeema is passionate about education, particularly to girls and she is the founder of BakiShule, an application that aims at preventing students from dropping out of school. Dr. Mduma has been among the advisors of a peer educators’ group that voluntarily provides education to the youth and other people around the community, at no cost to the beneficiaries. As part of the community work, Neema organizes free training and workshops on the role of girls in data science, machine learning and artificial intelligence. \r\n\r\nThe workshops and training aim to encourage exploration of technology, promote self-confidence, and support aspiration for technical careers among girl students. In 2020, Dr. Mduma has been selected as one of the twenty “Young Talents” of the L’Oréal-UNESCO For Women in Science regional Programme in Sub-Saharan Africa for her research project on \"Data-Driven Approach for Predicting Student Dropout in Secondary Schools','https://tz.linkedin.com/in/mduma','https://twitter.com/nakadori?lang=en','0','neema.mduma@ai4dlab.or.tz',1,'team/Dr_Mduma.jpg','2023-02-08 17:05:05.454533','2023-02-08 17:05:05.454541','Nelson Mandela Institute of Science and Technology'),(13,'Dr. Tabu','S. Kondo','Researcher - Healthcare','Tabu S. Kondo is a Lecturer and Head, Department of Computer Science and Engineering at the College of Informatics and Virtual Education of the University of Dodoma, Tanzania. He received his BSc degree in Computer Science from International University of Africa, Khartoum, Sudan in 2004, MSc degree in Computer Science and PhD degree in Computer Science from the University of Dodoma, Tanzania in 2011 and 2016 respectively. His research and teaching interest areas include but are not limited to e-Learning, technology adoption, cyber security and forensics, Artificial Intelligence, and Internet of Things.','https://www.linkedin.com/in/tabu-kondo-74aaa5133/','#','0','tabu.kondo@ai4dlab.or.tz',1,'team/Dr_Kondo.jpg','2023-02-08 17:07:04.531412','2023-02-08 17:07:04.531438','The University of Dodoma'),(14,'Dr. Ramadhani','Sinde','Researcher - Environment Conservation and Agriculture','Ramadhani Sinde receives his BSc and MSc in Engineering and Technologies in Telecommunication (Moscow Technical University of Communication and Informatics), Postgraduate Diploma in Wireless and Mobile Computing (Center for Development of Advanced Computing, India) and PhD in Information and Communication Science and Engineering (NM-AIST). \r\n\r\nHe has authored and co-authored more than 20 papers in internationally refereed journals and conferences. He specializes in Electronics and Telecommunication Engineering and his research interests are Telecommunications engineering; Deep Reinforcement Learning, Wireless Sensor Networks; Internet of Things and Embedded Systems.','https://www.linkedin.com/in/ramadhani-sinde-25a34659/','https://twitter.com/ramadhani_sinde','0','ramadhani.sinde@ai4dlab.or.tz',1,'team/Mr_Sinde.jpg','2023-02-08 17:09:45.968694','2023-02-08 17:09:45.968707','Nelson Mandela African Institute of Science and Technoloy'),(18,'Dr. Noe Elisa','Nnko','Researcher - Infrastructure and Data Ecosystem','Noe Elisa received his Ph.D. degree in Cyber Security with Artificial Intelligence from Northumbria University, UK, in 2021, under the support of the Commonwealth Scholarships commission in the UK. Prior to that, he received his M.Tech degree in Computer Networks and Information Security from Jawaharlal Nehru Technological University, India, in 2014. \r\n\r\nHe also received a B.Sc degree in Telecommunication Engineering from the University of Dar es salaam, Tanzania in 2010. Dr. Noe has more than ten years of teaching experience with the University of Dodoma, Tanzania, where he worked as a lecturer. His research interests include artificial intelligence, computational intelligence, machine learning, information security, privacy assurance, e-Government systems, smart cities, blockchain technology, human-computer interaction and cloud computing. He has about 15 publications in the domain of computational intelligence and cyber security.','https://www.linkedin.com/in/noe-elisa-ph-d-7793ab55/?originalSubdomain=tz','https://twitter.com/NoeElisa1','255762865160','noe.elisa@ai4dlab.or.tz',1,'team/Mr_Noe.jpg','2023-02-08 22:42:17.829064','2023-02-08 22:42:17.829075','The University of Dodoma');
/*!40000 ALTER TABLE `team_team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-09  1:51:14
