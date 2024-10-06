-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ventadejuegos
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `carrito`
--

DROP TABLE IF EXISTS `carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito` (
  `idCarrito` int NOT NULL AUTO_INCREMENT,
  `Usuario_idUsuario` int DEFAULT NULL,
  PRIMARY KEY (`idCarrito`),
  KEY `Usuario_idUsuario` (`Usuario_idUsuario`),
  CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito`
--

LOCK TABLES `carrito` WRITE;
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
INSERT INTO `carrito` VALUES (13,2),(1,4),(4,4),(10,6),(9,7),(12,7),(3,8),(7,8),(11,8),(14,8),(5,9),(15,9),(6,12),(8,13),(2,15);
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrito_has_juego`
--

DROP TABLE IF EXISTS `carrito_has_juego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito_has_juego` (
  `Carrito_idCarrito` int NOT NULL,
  `Juego_idJuego` int NOT NULL,
  PRIMARY KEY (`Carrito_idCarrito`,`Juego_idJuego`),
  KEY `Juego_idJuego` (`Juego_idJuego`),
  CONSTRAINT `carrito_has_juego_ibfk_1` FOREIGN KEY (`Carrito_idCarrito`) REFERENCES `carrito` (`idCarrito`),
  CONSTRAINT `carrito_has_juego_ibfk_2` FOREIGN KEY (`Juego_idJuego`) REFERENCES `juego` (`idJuego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito_has_juego`
--

LOCK TABLES `carrito_has_juego` WRITE;
/*!40000 ALTER TABLE `carrito_has_juego` DISABLE KEYS */;
INSERT INTO `carrito_has_juego` VALUES (7,1),(10,2),(14,2),(2,3),(9,3),(6,4),(11,4),(8,5),(1,6),(5,6),(4,7),(13,7),(15,7),(3,8),(12,8);
/*!40000 ALTER TABLE `carrito_has_juego` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `idCategoria` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) NOT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Accion'),(2,'Terror'),(3,'Plataformas'),(4,'Puzzle'),(5,'Lucha'),(6,'Shooter');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `idCompra` int NOT NULL AUTO_INCREMENT,
  `Usuario_idUsuario` int DEFAULT NULL,
  `Juego_idJuego` int DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idCompra`),
  KEY `Usuario_idUsuario` (`Usuario_idUsuario`),
  KEY `Juego_idJuego` (`Juego_idJuego`),
  CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`),
  CONSTRAINT `compra_ibfk_2` FOREIGN KEY (`Juego_idJuego`) REFERENCES `juego` (`idJuego`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,4,6,'2023-06-12 00:00:00',204.00),(2,15,3,'2023-07-24 00:00:00',450.00),(3,8,8,'2023-08-22 00:00:00',220.00),(4,4,7,'2024-08-28 00:00:00',228.00),(5,9,6,'2023-11-19 00:00:00',204.00),(6,12,4,'2023-12-24 00:00:00',320.00),(7,8,1,'2024-01-27 00:00:00',240.00),(8,13,5,'2024-02-12 00:00:00',144.00),(9,7,3,'2024-02-22 00:00:00',450.00),(10,6,2,'2024-03-12 00:00:00',90.00),(11,8,4,'2024-04-11 00:00:00',320.00),(12,7,8,'2024-04-19 00:00:00',220.00),(13,2,7,'2024-05-21 00:00:00',228.00),(14,8,2,'2024-06-12 00:00:00',150.00),(15,9,7,'2024-09-25 00:00:00',228.00);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juego`
--

DROP TABLE IF EXISTS `juego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juego` (
  `idJuego` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `Categoria_idCategoria` int DEFAULT NULL,
  PRIMARY KEY (`idJuego`),
  KEY `Categoria_idCategoria` (`Categoria_idCategoria`),
  CONSTRAINT `juego_ibfk_1` FOREIGN KEY (`Categoria_idCategoria`) REFERENCES `categoria` (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juego`
--

LOCK TABLES `juego` WRITE;
/*!40000 ALTER TABLE `juego` DISABLE KEYS */;
INSERT INTO `juego` VALUES (1,'Pac-Man',240.00,4),(2,'Super Mario Bros',150.00,3),(3,'Street Fighter',450.00,5),(4,'Tomb Raider',320.00,3),(5,'Counter Strike',240.00,6),(6,'Doom',340.00,6),(7,'Mortal Kombat',380.00,5),(8,'Half Life',220.00,6),(9,'Resident Evil',360.00,2);
/*!40000 ALTER TABLE `juego` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membresia`
--

DROP TABLE IF EXISTS `membresia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membresia` (
  `idMembresia` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) NOT NULL,
  `descuento` decimal(5,2) NOT NULL,
  PRIMARY KEY (`idMembresia`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membresia`
--

LOCK TABLES `membresia` WRITE;
/*!40000 ALTER TABLE `membresia` DISABLE KEYS */;
INSERT INTO `membresia` VALUES (1,'plus',40.00),(2,'standard',0.00);
/*!40000 ALTER TABLE `membresia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `Membresia_idMembresia` int DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `email` (`email`),
  KEY `Membresia_idMembresia` (`Membresia_idMembresia`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`Membresia_idMembresia`) REFERENCES `membresia` (`idMembresia`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'messi@gmail.com','Messi10','Lionel','Messi',1),(2,'dibu@gmail.com','Dibu01','Emiliano','Martinez',1),(3,'montiel@gmail.com','Somosmontiel1','Gonzalo','Montiel',2),(4,'depaul@gmail.com','Garra25','Rodrigo','De Paul',1),(5,'otamendi@gmail.com','Muro22','Nicolas','Otamendi',2),(6,'alvarez@gmail.com','Araña09','Julian','Alvarez',1),(7,'cuti@gmail.com','Nopasaras1','Cristian','Romero',2),(8,'Martinez@gmail.com','Quite22','Lisandro','Martinez',2),(9,'toro@gmail.com','Goles58','Lautaro','Martinez',1),(10,'scaloni@gmail.com','Scaloneta22','Lionel','Scaloni',1),(11,'taglia@gmail.com','Lateral25','Nicolas','Tagliafico',2),(12,'fernandez@hotmail.com','Enzito23','Enzo','Fernandez',2),(13,'dimaria@yahoo.com','Fideo11','Angel','Di Maria',1),(14,'locelco@hotmail.com','Gio2424','Giovani','Lo Celso',2),(15,'Gonzalez@hotmail.com','Nico2527','Nicolas','Gonzalez',2);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-06  0:51:09
