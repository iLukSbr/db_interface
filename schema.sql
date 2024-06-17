-- MySQL dump 10.13  Distrib 8.3.0, for Win64 (x86_64)
--
-- Host: localhost    Database: materiais_de_construcao
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_endereco_primario` int NOT NULL,
  `id_endereco_secundario` int DEFAULT NULL,
  `foto` blob,
  `nome` varchar(255) NOT NULL,
  `sobrenome` varchar(255) NOT NULL,
  `nome_social` varchar(255) DEFAULT NULL,
  `genero` varchar(255) DEFAULT NULL,
  `estado_civil` varchar(255) DEFAULT NULL,
  `profissao` varchar(255) DEFAULT NULL,
  `razao_social_empresa` varchar(255) DEFAULT NULL,
  `cnpj` int DEFAULT NULL,
  `data_de_nascimento` date NOT NULL,
  `nacionalidade` varchar(255) DEFAULT NULL,
  `raca` enum('branca','preta','parda','indígena','amarela') DEFAULT NULL,
  `cpf` int NOT NULL,
  `data_de_emissao` date NOT NULL,
  `orgao_expedidor` varchar(255) NOT NULL,
  `numero_do_cartao_bancario` int DEFAULT NULL,
  `validade_do_cartao_bancario` date DEFAULT NULL,
  `cvv` int DEFAULT NULL,
  `credito` tinyint(1) DEFAULT NULL,
  `telefone_primario` int NOT NULL,
  `telefone_secundario` int DEFAULT NULL,
  `e_mail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `enderecos`
--

DROP TABLE IF EXISTS `enderecos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enderecos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `rua` varchar(255) NOT NULL,
  `numero` varchar(255) NOT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  `bairro` varchar(255) NOT NULL,
  `cidade` varchar(255) NOT NULL,
  `estado` varchar(255) NOT NULL,
  `pais` varchar(255) NOT NULL,
  `cep` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fotos`
--

DROP TABLE IF EXISTS `fotos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fotos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `foto` blob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `links_externos`
--

DROP TABLE IF EXISTS `links_externos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `links_externos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `link_externo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `manuais`
--

DROP TABLE IF EXISTS `manuais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manuais` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `manual` blob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_venda` int NOT NULL,
  `id_produto` int NOT NULL,
  `quantidade` int NOT NULL,
  `desconto` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_venda` (`id_venda`),
  KEY `id_produto` (`id_produto`),
  CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`id`),
  CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `precos`
--

DROP TABLE IF EXISTS `precos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `precos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `preco` double NOT NULL,
  `data_hora_de_inicio` datetime NOT NULL,
  `data_hora_de_termino` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_subtipo` int NOT NULL,
  `estoque` int NOT NULL,
  `peso` double NOT NULL,
  `tamanho_da_caixa_x` double NOT NULL,
  `tamanho_da_caixa_y` double NOT NULL,
  `tamanho_da_caixa_z` double NOT NULL,
  `maximo_de_caixas_empilhadas` int NOT NULL,
  `fragil` tinyint(1) NOT NULL,
  `perigoso` tinyint(1) NOT NULL,
  `validade` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `subtipos`
--

DROP TABLE IF EXISTS `subtipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subtipos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_tipo` int NOT NULL,
  `subtipo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tipos`
--

DROP TABLE IF EXISTS `tipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_endereco` int NOT NULL,
  `modo_de_pagamento` enum('boleto','pix','transferencia','cartao_de_credito','cartao_de_debito') DEFAULT NULL,
  `quantidade_de_parcelas` int NOT NULL,
  `juros` double DEFAULT NULL,
  `dia_de_vencimento` int DEFAULT NULL,
  `data_do_primeiro_vencimento` date NOT NULL,
  `data_hora_da_venda` datetime NOT NULL,
  `data_hora_de_entrega` datetime NOT NULL,
  `condicoes` text,
  `nota_fiscal` blob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_endereco` (`id_endereco`),
  CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  CONSTRAINT `vendas_ibfk_2` FOREIGN KEY (`id_endereco`) REFERENCES `enderecos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `video` blob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_diario`
--

DROP TABLE IF EXISTS `volume_vendas_diario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_diario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `dia` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_diario_estadual`
--

DROP TABLE IF EXISTS `volume_vendas_diario_estadual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_diario_estadual` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `dia` date DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_diario_municipal`
--

DROP TABLE IF EXISTS `volume_vendas_diario_municipal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_diario_municipal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `dia` date DEFAULT NULL,
  `municipio` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_mensal`
--

DROP TABLE IF EXISTS `volume_vendas_mensal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_mensal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `mes` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_mensal_estadual`
--

DROP TABLE IF EXISTS `volume_vendas_mensal_estadual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_mensal_estadual` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `mes` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_mensal_municipal`
--

DROP TABLE IF EXISTS `volume_vendas_mensal_municipal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_mensal_municipal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `mes` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `municipio` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_semanal`
--

DROP TABLE IF EXISTS `volume_vendas_semanal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_semanal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `semana` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_semanal_estadual`
--

DROP TABLE IF EXISTS `volume_vendas_semanal_estadual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_semanal_estadual` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `semana` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `volume_vendas_semanal_municipal`
--

DROP TABLE IF EXISTS `volume_vendas_semanal_municipal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volume_vendas_semanal_municipal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantidade` int NOT NULL,
  `semana` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `municipio` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-17  3:35:23
