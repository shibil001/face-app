/*
SQLyog Community v13.2.1 (64 bit)
MySQL - 10.4.28-MariaDB : Database - facerecognition
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`facerecognition` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `facerecognition`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add course',7,'add_course'),
(26,'Can change course',7,'change_course'),
(27,'Can delete course',7,'delete_course'),
(28,'Can view course',7,'view_course'),
(29,'Can add department',8,'add_department'),
(30,'Can change department',8,'change_department'),
(31,'Can delete department',8,'delete_department'),
(32,'Can view department',8,'view_department'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add subject',10,'add_subject'),
(38,'Can change subject',10,'change_subject'),
(39,'Can delete subject',10,'delete_subject'),
(40,'Can view subject',10,'view_subject'),
(41,'Can add timetable',11,'add_timetable'),
(42,'Can change timetable',11,'change_timetable'),
(43,'Can delete timetable',11,'delete_timetable'),
(44,'Can view timetable',11,'view_timetable'),
(45,'Can add student',12,'add_student'),
(46,'Can change student',12,'change_student'),
(47,'Can delete student',12,'delete_student'),
(48,'Can view student',12,'view_student'),
(49,'Can add attendance',13,'add_attendance'),
(50,'Can change attendance',13,'change_attendance'),
(51,'Can delete attendance',13,'delete_attendance'),
(52,'Can view attendance',13,'view_attendance');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(13,'myapp','attendance'),
(7,'myapp','course'),
(8,'myapp','department'),
(9,'myapp','login'),
(12,'myapp','student'),
(10,'myapp','subject'),
(11,'myapp','timetable'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-12-14 10:19:49.599472'),
(2,'auth','0001_initial','2023-12-14 10:19:54.991703'),
(3,'admin','0001_initial','2023-12-14 10:19:56.585044'),
(4,'admin','0002_logentry_remove_auto_add','2023-12-14 10:19:56.600829'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-12-14 10:19:56.631911'),
(6,'contenttypes','0002_remove_content_type_name','2023-12-14 10:19:57.022600'),
(7,'auth','0002_alter_permission_name_max_length','2023-12-14 10:19:57.522357'),
(8,'auth','0003_alter_user_email_max_length','2023-12-14 10:19:57.584813'),
(9,'auth','0004_alter_user_username_opts','2023-12-14 10:19:57.600592'),
(10,'auth','0005_alter_user_last_login_null','2023-12-14 10:19:58.053612'),
(11,'auth','0006_require_contenttypes_0002','2023-12-14 10:19:58.100314'),
(12,'auth','0007_alter_validators_add_error_messages','2023-12-14 10:19:58.115954'),
(13,'auth','0008_alter_user_username_max_length','2023-12-14 10:19:58.178564'),
(14,'auth','0009_alter_user_last_name_max_length','2023-12-14 10:19:58.256689'),
(15,'auth','0010_alter_group_name_max_length','2023-12-14 10:19:58.756572'),
(16,'auth','0011_update_proxy_permissions','2023-12-14 10:19:58.772190'),
(17,'auth','0012_alter_user_first_name_max_length','2023-12-14 10:19:58.803304'),
(18,'myapp','0001_initial','2023-12-14 10:20:02.212419'),
(19,'sessions','0001_initial','2023-12-14 10:20:02.524847'),
(20,'myapp','0002_login_type','2023-12-14 10:31:31.730721'),
(21,'myapp','0003_student_login','2024-01-12 11:20:30.744369'),
(22,'myapp','0004_student_email','2024-01-12 11:23:52.467461'),
(23,'myapp','0005_alter_attendance_student','2024-01-15 08:47:10.215592'),
(24,'myapp','0006_alter_attendance_attendance_alter_student_phone','2024-01-15 09:47:32.959743'),
(25,'myapp','0007_attendance_time','2024-01-15 11:18:46.803023'),
(26,'myapp','0008_student_sem','2024-01-19 10:03:08.432706');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('6o35dtstafzt3dfpc0pxx123k91z6idu','eyJsaWQiOjF9:1rQnIA:fR3ThOubhme2IhQe-wukW9t4wu89H0wvlgwoASgYklI','2024-02-02 11:44:10.876489'),
('93d15cltimb8d33b5vzhz7sohgpe49p6','eyJsaWQiOjF9:1rPJch:CO2soFYIoL_SS21t6vHEy5G9AZB6Bx_WwhvgGMn61H4','2024-01-29 09:51:15.914355'),
('ldfk92rvr0mshblpko0b1gh0fgqwav7p','eyJsaWQiOjF9:1rDjKH:b3x-9QQOy49lTlJZ6_G1C9wZGVNTzyt9Rl_CzF92JE4','2023-12-28 10:52:21.337942');

/*Table structure for table `myapp_attendance` */

DROP TABLE IF EXISTS `myapp_attendance`;

CREATE TABLE `myapp_attendance` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Attendance` varchar(100) NOT NULL,
  `Hour` varchar(100) NOT NULL,
  `STUDENT_id` bigint(20) NOT NULL,
  `Time` time(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_attendance_STUDENT_id_d2e99675_fk_myapp_student_id` (`STUDENT_id`),
  CONSTRAINT `myapp_attendance_STUDENT_id_d2e99675_fk_myapp_student_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `myapp_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_attendance` */

insert  into `myapp_attendance`(`id`,`Date`,`Attendance`,`Hour`,`STUDENT_id`,`Time`) values 
(28,'2024-01-15','','6',13,'12:10:00.000000'),
(29,'2024-01-15','Absent','5',13,'12:10:00.000000'),
(30,'2024-01-15','Absent','5',14,'12:10:00.000000'),
(31,'2024-01-15','Absent','5',15,'12:10:00.000000'),
(32,'2024-01-15','','6',14,'12:10:00.000000'),
(33,'2024-01-15','','6',15,'12:10:00.000000'),
(34,'2024-01-19','Present','6',13,'17:07:24.000000'),
(35,'2024-01-19','Absent','5',13,'17:07:24.000000'),
(36,'2024-01-19','Absent','5',14,'17:07:24.000000'),
(37,'2024-01-19','Absent','5',15,'17:07:24.000000'),
(38,'2024-01-19','Absent','5',16,'17:07:24.000000'),
(39,'2024-01-19','Present','6',14,'17:07:39.000000');

/*Table structure for table `myapp_course` */

DROP TABLE IF EXISTS `myapp_course`;

CREATE TABLE `myapp_course` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `CourseName` varchar(100) NOT NULL,
  `TotalSem` varchar(100) NOT NULL,
  `DEPARTMENT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_course_DEPARTMENT_id_9a598a92_fk_myapp_department_id` (`DEPARTMENT_id`),
  CONSTRAINT `myapp_course_DEPARTMENT_id_9a598a92_fk_myapp_department_id` FOREIGN KEY (`DEPARTMENT_id`) REFERENCES `myapp_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_course` */

insert  into `myapp_course`(`id`,`CourseName`,`TotalSem`,`DEPARTMENT_id`) values 
(3,'cs','6',5),
(4,'a','4',5),
(5,'b','6',5),
(6,'cs','6',5),
(7,'stati','6',9),
(8,'BCA','6',5);

/*Table structure for table `myapp_department` */

DROP TABLE IF EXISTS `myapp_department`;

CREATE TABLE `myapp_department` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_department` */

insert  into `myapp_department`(`id`,`DepartmentName`) values 
(5,'computersciences'),
(6,'bca'),
(7,'cs'),
(9,'stati'),
(10,'cs');

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','hi','admin'),
(4,'shibil@gmail.com','9887988798','student'),
(5,'irfan@gmail.com','8987878787','student'),
(6,'shammas@gmail.com','7898989898','student'),
(7,'diya@gmail.com','9887988776','student');

/*Table structure for table `myapp_student` */

DROP TABLE IF EXISTS `myapp_student`;

CREATE TABLE `myapp_student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Image` varchar(250) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Pin` int(11) NOT NULL,
  `Post` varchar(100) NOT NULL,
  `Phone` bigint(20) NOT NULL,
  `HouseName` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `ParentName` varchar(100) NOT NULL,
  `ParentPhone` bigint(20) NOT NULL,
  `COURSE_id` bigint(20) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Sem` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_student_COURSE_id_5fe98c90_fk_myapp_course_id` (`COURSE_id`),
  KEY `myapp_student_LOGIN_id_d3327a2f_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_student_COURSE_id_5fe98c90_fk_myapp_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `myapp_course` (`id`),
  CONSTRAINT `myapp_student_LOGIN_id_d3327a2f_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_student` */

insert  into `myapp_student`(`id`,`Name`,`Image`,`Gender`,`DOB`,`Pin`,`Post`,`Phone`,`HouseName`,`Place`,`ParentName`,`ParentPhone`,`COURSE_id`,`LOGIN_id`,`Email`,`Sem`) values 
(13,'shibil','/media/20240115-150353.jpg','Male','2024-01-03',678767,'mukkam',2147483647,'kuchikattil','areekode','asker',9898988798,8,4,'shibil@gmail.com','1'),
(14,'irfan','/media/20240115-150502.jpg','Male','2024-01-02',989898,'moikal',8747483647,'kad','cheruvatta','kkkkk',9898786787,3,5,'irfan@gmail.com','6'),
(15,'shammas','/media/20240119-171446.jpg','Male','2024-01-03',678098,'aramabram',9147483647,'arambram,','koduvally','kkkks',9878987867,3,6,'shammas@gmail.com','1'),
(16,'diya','/media/20240119-153833.jpg','Female','2024-01-03',673567,'balussery',9887988776,'kaad','balussery','abdulla',8978675656,8,7,'diya@gmail.com','6');

/*Table structure for table `myapp_subject` */

DROP TABLE IF EXISTS `myapp_subject`;

CREATE TABLE `myapp_subject` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `SubjectName` varchar(100) NOT NULL,
  `Semester` varchar(100) NOT NULL,
  `COURSE_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_subject_COURSE_id_344c7664_fk_myapp_course_id` (`COURSE_id`),
  CONSTRAINT `myapp_subject_COURSE_id_344c7664_fk_myapp_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `myapp_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_subject` */

insert  into `myapp_subject`(`id`,`SubjectName`,`Semester`,`COURSE_id`) values 
(4,'english','2',3),
(6,'malayalam','2',3),
(7,'english','2',7),
(8,'maths','1',3),
(9,'python','3',3),
(10,'coa','4',3),
(11,'sensor','5',3),
(12,'graphics','6',3);

/*Table structure for table `myapp_timetable` */

DROP TABLE IF EXISTS `myapp_timetable`;

CREATE TABLE `myapp_timetable` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Day` varchar(100) NOT NULL,
  `Hour` varchar(100) NOT NULL,
  `SUBJECT_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_timetable_SUBJECT_id_259fa3fd_fk_myapp_subject_id` (`SUBJECT_id`),
  CONSTRAINT `myapp_timetable_SUBJECT_id_259fa3fd_fk_myapp_subject_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `myapp_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_timetable` */

insert  into `myapp_timetable`(`id`,`Day`,`Hour`,`SUBJECT_id`) values 
(3,'thusday','1',4),
(5,'wednesday','2',4),
(6,'monday','00:00',4),
(7,'monday','00:08',4),
(8,'monday','1',4),
(9,'monday','2',6),
(10,'monday','3',6),
(11,'monday','4',6),
(12,'monday','6',7),
(13,'tuesday','1',8),
(14,'thusday','4',9),
(15,'monday','3',9),
(16,'wednesday','5',10),
(17,'thusday','2',10),
(18,'friday','6',10),
(19,'tuesday','4',11),
(20,'monday','1',11),
(21,'thusday','5',12),
(22,'monday','4',12),
(23,'friday','7',12);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
