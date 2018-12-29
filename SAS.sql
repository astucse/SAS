-- MySQL dump 10.16  Distrib 10.1.37-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: SAS
-- ------------------------------------------------------
-- Server version	10.1.37-MariaDB-3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_department`
--

DROP TABLE IF EXISTS `account_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_department_school_id_7adceeaf_fk_account_school_id` (`school_id`),
  CONSTRAINT `account_department_school_id_7adceeaf_fk_account_school_id` FOREIGN KEY (`school_id`) REFERENCES `account_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_department`
--

LOCK TABLES `account_department` WRITE;
/*!40000 ALTER TABLE `account_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_school`
--

DROP TABLE IF EXISTS `account_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_school`
--

LOCK TABLES `account_school` WRITE;
/*!40000 ALTER TABLE `account_school` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_student`
--

DROP TABLE IF EXISTS `account_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(12) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `year` int(10) unsigned NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`),
  UNIQUE KEY `school_id` (`school_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_student_department_id_d905c079_fk_account_department_id` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`),
  CONSTRAINT `account_student_school_id_fb6e487f_fk_account_school_id` FOREIGN KEY (`school_id`) REFERENCES `account_school` (`id`),
  CONSTRAINT `account_student_user_id_cbbf6595_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_student`
--

LOCK TABLES `account_student` WRITE;
/*!40000 ALTER TABLE `account_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_subject`
--

DROP TABLE IF EXISTS `account_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_subject_department_id_300ebf14_fk_account_department_id` (`department_id`),
  CONSTRAINT `account_subject_department_id_300ebf14_fk_account_department_id` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_subject`
--

LOCK TABLES `account_subject` WRITE;
/*!40000 ALTER TABLE `account_subject` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_teacher`
--

DROP TABLE IF EXISTS `account_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(12) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_teacher_department_id_b3c60f02_fk_account_department_id` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`),
  CONSTRAINT `account_teacher_user_id_d5e250bb_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_teacher`
--

LOCK TABLES `account_teacher` WRITE;
/*!40000 ALTER TABLE `account_teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add department',1,'add_department'),(2,'Can change department',1,'change_department'),(3,'Can delete department',1,'delete_department'),(4,'Can view department',1,'view_department'),(5,'Can add exam',2,'add_exam'),(6,'Can change exam',2,'change_exam'),(7,'Can delete exam',2,'delete_exam'),(8,'Can view exam',2,'view_exam'),(9,'Can add question',3,'add_question'),(10,'Can change question',3,'change_question'),(11,'Can delete question',3,'delete_question'),(12,'Can view question',3,'view_question'),(13,'Can add school',4,'add_school'),(14,'Can change school',4,'change_school'),(15,'Can delete school',4,'delete_school'),(16,'Can view school',4,'view_school'),(17,'Can add student',5,'add_student'),(18,'Can change student',5,'change_student'),(19,'Can delete student',5,'delete_student'),(20,'Can view student',5,'view_student'),(21,'Can add subject',6,'add_subject'),(22,'Can change subject',6,'change_subject'),(23,'Can delete subject',6,'delete_subject'),(24,'Can view subject',6,'view_subject'),(25,'Can add teacher',7,'add_teacher'),(26,'Can change teacher',7,'change_teacher'),(27,'Can delete teacher',7,'delete_teacher'),(28,'Can view teacher',7,'view_teacher'),(29,'Can add videos',8,'add_videos'),(30,'Can change videos',8,'change_videos'),(31,'Can delete videos',8,'delete_videos'),(32,'Can view videos',8,'view_videos'),(33,'Can add log entry',9,'add_logentry'),(34,'Can change log entry',9,'change_logentry'),(35,'Can delete log entry',9,'delete_logentry'),(36,'Can view log entry',9,'view_logentry'),(37,'Can add permission',10,'add_permission'),(38,'Can change permission',10,'change_permission'),(39,'Can delete permission',10,'delete_permission'),(40,'Can view permission',10,'view_permission'),(41,'Can add group',11,'add_group'),(42,'Can change group',11,'change_group'),(43,'Can delete group',11,'delete_group'),(44,'Can view group',11,'view_group'),(45,'Can add user',12,'add_user'),(46,'Can change user',12,'change_user'),(47,'Can delete user',12,'delete_user'),(48,'Can view user',12,'view_user'),(49,'Can add content type',13,'add_contenttype'),(50,'Can change content type',13,'change_contenttype'),(51,'Can delete content type',13,'delete_contenttype'),(52,'Can view content type',13,'view_contenttype'),(53,'Can add session',14,'add_session'),(54,'Can change session',14,'change_session'),(55,'Can delete session',14,'delete_session'),(56,'Can view session',14,'view_session'),(57,'Can add subject',15,'add_subject'),(58,'Can change subject',15,'change_subject'),(59,'Can delete subject',15,'delete_subject'),(60,'Can view subject',15,'view_subject'),(61,'Can add teacher',16,'add_teacher'),(62,'Can change teacher',16,'change_teacher'),(63,'Can delete teacher',16,'delete_teacher'),(64,'Can view teacher',16,'view_teacher'),(65,'Can add department',17,'add_department'),(66,'Can change department',17,'change_department'),(67,'Can delete department',17,'delete_department'),(68,'Can view department',17,'view_department'),(69,'Can add school',18,'add_school'),(70,'Can change school',18,'change_school'),(71,'Can delete school',18,'delete_school'),(72,'Can view school',18,'view_school'),(73,'Can add student',19,'add_student'),(74,'Can change student',19,'change_student'),(75,'Can delete student',19,'delete_student'),(76,'Can view student',19,'view_student'),(77,'Can add choice',20,'add_choice'),(78,'Can change choice',20,'change_choice'),(79,'Can delete choice',20,'delete_choice'),(80,'Can view choice',20,'view_choice');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$WCAaGlGgWAlD$YL78oEHIF9I2WDx06x12D2zOeiHPmG+ryCqgOE3fMqE=','2018-12-24 04:12:30.412578',1,'admin','','','',1,1,'2018-12-24 04:12:26.570326');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (17,'account','department'),(18,'account','school'),(19,'account','student'),(15,'account','subject'),(16,'account','teacher'),(9,'admin','logentry'),(11,'auth','group'),(10,'auth','permission'),(12,'auth','user'),(13,'contenttypes','contenttype'),(20,'resources','choice'),(1,'resources','department'),(2,'resources','exam'),(3,'resources','question'),(4,'resources','school'),(5,'resources','student'),(6,'resources','subject'),(7,'resources','teacher'),(8,'resources','videos'),(14,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-12-24 04:09:06.934726'),(2,'auth','0001_initial','2018-12-24 04:09:14.443203'),(3,'admin','0001_initial','2018-12-24 04:09:16.126185'),(4,'admin','0002_logentry_remove_auto_add','2018-12-24 04:09:16.166606'),(5,'admin','0003_logentry_add_action_flag_choices','2018-12-24 04:09:16.242755'),(6,'contenttypes','0002_remove_content_type_name','2018-12-24 04:09:17.106427'),(7,'auth','0002_alter_permission_name_max_length','2018-12-24 04:09:17.797722'),(8,'auth','0003_alter_user_email_max_length','2018-12-24 04:09:18.532508'),(9,'auth','0004_alter_user_username_opts','2018-12-24 04:09:18.585221'),(10,'auth','0005_alter_user_last_login_null','2018-12-24 04:09:19.110811'),(11,'auth','0006_require_contenttypes_0002','2018-12-24 04:09:19.143928'),(12,'auth','0007_alter_validators_add_error_messages','2018-12-24 04:09:19.184905'),(13,'auth','0008_alter_user_username_max_length','2018-12-24 04:09:19.835456'),(14,'auth','0009_alter_user_last_name_max_length','2018-12-24 04:09:20.492497'),(15,'resources','0001_initial','2018-12-24 04:09:33.553444'),(16,'sessions','0001_initial','2018-12-24 04:09:34.109217'),(17,'account','0001_initial','2018-12-24 06:45:38.411312'),(18,'resources','0002_auto_20181224_0645','2018-12-24 06:45:49.893533'),(19,'resources','0003_auto_20181228_1733','2018-12-28 17:33:10.715573');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('t2hycx28txhf26b4onflb46t1ainpkql','YjM0YTlhZmU0MGRjNjYxZWI3MzIxNTM4YjM0YTFkOGY0ODM1MjNmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxODkwYmU3ZmMzZDM0ZmIxOTU4ZDk5ZmMxNTgzZTZjZGIzNmMyNzdhIn0=','2019-01-07 04:12:30.448879');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_choice`
--

DROP TABLE IF EXISTS `resources_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` longtext NOT NULL,
  `answer_to_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resources_choice_answer_to_id_47d0ce70_fk_resources_question_id` (`answer_to_id`),
  KEY `resources_choice_question_id_2b659748_fk_resources_question_id` (`question_id`),
  CONSTRAINT `resources_choice_answer_to_id_47d0ce70_fk_resources_question_id` FOREIGN KEY (`answer_to_id`) REFERENCES `resources_question` (`id`),
  CONSTRAINT `resources_choice_question_id_2b659748_fk_resources_question_id` FOREIGN KEY (`question_id`) REFERENCES `resources_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_choice`
--

LOCK TABLES `resources_choice` WRITE;
/*!40000 ALTER TABLE `resources_choice` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_choice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_exam`
--

DROP TABLE IF EXISTS `resources_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(250) NOT NULL,
  `department_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resources_exam_department_id_97539146_fk_account_department_id` (`department_id`),
  KEY `resources_exam_subject_id_2ba8eff0_fk_account_subject_id` (`subject_id`),
  CONSTRAINT `resources_exam_department_id_97539146_fk_account_department_id` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`),
  CONSTRAINT `resources_exam_subject_id_2ba8eff0_fk_account_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `account_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_exam`
--

LOCK TABLES `resources_exam` WRITE;
/*!40000 ALTER TABLE `resources_exam` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_question`
--

DROP TABLE IF EXISTS `resources_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` longtext NOT NULL,
  `type` varchar(50) NOT NULL,
  `explanation` longtext NOT NULL,
  `hint` longtext NOT NULL,
  `date_uploaded` date NOT NULL,
  `department_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resources_question_department_id_8c24b24e_fk_account_d` (`department_id`),
  KEY `resources_question_subject_id_278b522f_fk_account_subject_id` (`subject_id`),
  CONSTRAINT `resources_question_department_id_8c24b24e_fk_account_d` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`),
  CONSTRAINT `resources_question_subject_id_278b522f_fk_account_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `account_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_question`
--

LOCK TABLES `resources_question` WRITE;
/*!40000 ALTER TABLE `resources_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_videos`
--

DROP TABLE IF EXISTS `resources_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(250) NOT NULL,
  `name` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resources_videos_department_id_c5297919_fk_account_department_id` (`department_id`),
  KEY `resources_videos_subject_id_05a62d25_fk_account_subject_id` (`subject_id`),
  CONSTRAINT `resources_videos_department_id_c5297919_fk_account_department_id` FOREIGN KEY (`department_id`) REFERENCES `account_department` (`id`),
  CONSTRAINT `resources_videos_subject_id_05a62d25_fk_account_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `account_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_videos`
--

LOCK TABLES `resources_videos` WRITE;
/*!40000 ALTER TABLE `resources_videos` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-28 20:33:29
