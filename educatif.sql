-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 30 mars 2026 à 22:47
-- Version du serveur : 8.0.39
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `educatif`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin_app_documentencadreur`
--

DROP TABLE IF EXISTS `admin_app_documentencadreur`;
CREATE TABLE IF NOT EXISTS `admin_app_documentencadreur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_document` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fichier` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_upload` datetime(6) NOT NULL,
  `valide` tinyint(1) NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `commentaire_admin` longtext COLLATE utf8mb4_unicode_ci,
  `date_validation` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_app_documentencadr_encadreur_id_type_docume_650d4e8c_uniq` (`encadreur_id`,`type_document`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `admin_app_sanction`
--

DROP TABLE IF EXISTS `admin_app_sanction`;
CREATE TABLE IF NOT EXISTS `admin_app_sanction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_sanction` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `commentaire` longtext COLLATE utf8mb4_unicode_ci,
  `date_sanction` datetime(6) NOT NULL,
  `actif` tinyint(1) NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `date_fin` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_app_sanction_encadreur_id_eae7655a_fk_utilisate` (`encadreur_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `admin_app_signalement`
--

DROP TABLE IF EXISTS `admin_app_signalement`;
CREATE TABLE IF NOT EXISTS `admin_app_signalement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_signalement` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_signalement` datetime(6) NOT NULL,
  `traite` tinyint(1) NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `commentaire_traitement` longtext COLLATE utf8mb4_unicode_ci,
  `date_traitement` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_app_signalemen_encadreur_id_ef58bfd2_fk_utilisate` (`encadreur_id`),
  KEY `admin_app_signalemen_utilisateur_id_856f7a69_fk_utilisate` (`utilisateur_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 3, 'add_permission'),
(6, 'Can change permission', 3, 'change_permission'),
(7, 'Can delete permission', 3, 'delete_permission'),
(8, 'Can view permission', 3, 'view_permission'),
(9, 'Can add group', 2, 'add_group'),
(10, 'Can change group', 2, 'change_group'),
(11, 'Can delete group', 2, 'delete_group'),
(12, 'Can view group', 2, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 10, 'add_utilisateur'),
(22, 'Can change user', 10, 'change_utilisateur'),
(23, 'Can delete user', 10, 'delete_utilisateur'),
(24, 'Can view user', 10, 'view_utilisateur'),
(25, 'Can add apprenant', 6, 'add_apprenant'),
(26, 'Can change apprenant', 6, 'change_apprenant'),
(27, 'Can delete apprenant', 6, 'delete_apprenant'),
(28, 'Can view apprenant', 6, 'view_apprenant'),
(29, 'Can add encadreur', 8, 'add_encadreur'),
(30, 'Can change encadreur', 8, 'change_encadreur'),
(31, 'Can delete encadreur', 8, 'delete_encadreur'),
(32, 'Can view encadreur', 8, 'view_encadreur'),
(33, 'Can add document verification', 7, 'add_documentverification'),
(34, 'Can change document verification', 7, 'change_documentverification'),
(35, 'Can delete document verification', 7, 'delete_documentverification'),
(36, 'Can view document verification', 7, 'view_documentverification'),
(37, 'Can add enfant', 9, 'add_enfant'),
(38, 'Can change enfant', 9, 'change_enfant'),
(39, 'Can delete enfant', 9, 'delete_enfant'),
(40, 'Can view enfant', 9, 'view_enfant'),
(41, 'Can add localisation', 11, 'add_localisation'),
(42, 'Can change localisation', 11, 'change_localisation'),
(43, 'Can delete localisation', 11, 'delete_localisation'),
(44, 'Can view localisation', 11, 'view_localisation'),
(45, 'Can add matiere', 12, 'add_matiere'),
(46, 'Can change matiere', 12, 'change_matiere'),
(47, 'Can delete matiere', 12, 'delete_matiere'),
(48, 'Can view matiere', 12, 'view_matiere'),
(49, 'Can add niveau', 13, 'add_niveau'),
(50, 'Can change niveau', 13, 'change_niveau'),
(51, 'Can delete niveau', 13, 'delete_niveau'),
(52, 'Can view niveau', 13, 'view_niveau'),
(53, 'Can add specialisation', 15, 'add_specialisation'),
(54, 'Can change specialisation', 15, 'change_specialisation'),
(55, 'Can delete specialisation', 15, 'delete_specialisation'),
(56, 'Can view specialisation', 15, 'view_specialisation'),
(57, 'Can add serie', 14, 'add_serie'),
(58, 'Can change serie', 14, 'change_serie'),
(59, 'Can delete serie', 14, 'delete_serie'),
(60, 'Can view serie', 14, 'view_serie'),
(61, 'Can add demande cours', 16, 'add_demandecours'),
(62, 'Can change demande cours', 16, 'change_demandecours'),
(63, 'Can delete demande cours', 16, 'delete_demandecours'),
(64, 'Can view demande cours', 16, 'view_demandecours'),
(65, 'Can add avis', 17, 'add_avis'),
(66, 'Can change avis', 17, 'change_avis'),
(67, 'Can delete avis', 17, 'delete_avis'),
(68, 'Can view avis', 17, 'view_avis'),
(69, 'Can add message', 18, 'add_message'),
(70, 'Can change message', 18, 'change_message'),
(71, 'Can delete message', 18, 'delete_message'),
(72, 'Can view message', 18, 'view_message'),
(73, 'Can add notification', 19, 'add_notification'),
(74, 'Can change notification', 19, 'change_notification'),
(75, 'Can delete notification', 19, 'delete_notification'),
(76, 'Can view notification', 19, 'view_notification'),
(77, 'Can add abonnement encadreur', 20, 'add_abonnementencadreur'),
(78, 'Can change abonnement encadreur', 20, 'change_abonnementencadreur'),
(79, 'Can delete abonnement encadreur', 20, 'delete_abonnementencadreur'),
(80, 'Can view abonnement encadreur', 20, 'view_abonnementencadreur'),
(81, 'Can add document encadreur', 21, 'add_documentencadreur'),
(82, 'Can change document encadreur', 21, 'change_documentencadreur'),
(83, 'Can delete document encadreur', 21, 'delete_documentencadreur'),
(84, 'Can view document encadreur', 21, 'view_documentencadreur'),
(85, 'Can add sanction', 22, 'add_sanction'),
(86, 'Can change sanction', 22, 'change_sanction'),
(87, 'Can delete sanction', 22, 'delete_sanction'),
(88, 'Can view sanction', 22, 'view_sanction'),
(89, 'Can add signalement', 23, 'add_signalement'),
(90, 'Can change signalement', 23, 'change_signalement'),
(91, 'Can delete signalement', 23, 'delete_signalement'),
(92, 'Can view signalement', 23, 'view_signalement'),
(93, 'Can add abonnement', 24, 'add_abonnement'),
(94, 'Can change abonnement', 24, 'change_abonnement'),
(95, 'Can delete abonnement', 24, 'delete_abonnement'),
(96, 'Can view abonnement', 24, 'view_abonnement'),
(97, 'Can add transaction', 25, 'add_transaction'),
(98, 'Can change transaction', 25, 'change_transaction'),
(99, 'Can delete transaction', 25, 'delete_transaction'),
(100, 'Can view transaction', 25, 'view_transaction'),
(101, 'Can add verification document', 26, 'add_verificationdocument'),
(102, 'Can change verification document', 26, 'change_verificationdocument'),
(103, 'Can delete verification document', 26, 'delete_verificationdocument'),
(104, 'Can view verification document', 26, 'view_verificationdocument'),
(105, 'Can add Classe', 27, 'add_classe'),
(106, 'Can change Classe', 27, 'change_classe'),
(107, 'Can delete Classe', 27, 'delete_classe'),
(108, 'Can view Classe', 27, 'view_classe'),
(109, 'Can add specialisation', 28, 'add_specialisation'),
(110, 'Can change specialisation', 28, 'change_specialisation'),
(111, 'Can delete specialisation', 28, 'delete_specialisation'),
(112, 'Can view specialisation', 28, 'view_specialisation');

-- --------------------------------------------------------

--
-- Structure de la table `avis_avis`
--

DROP TABLE IF EXISTS `avis_avis`;
CREATE TABLE IF NOT EXISTS `avis_avis` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `note` smallint UNSIGNED NOT NULL,
  `commentaire` longtext COLLATE utf8mb4_unicode_ci,
  `date_creation` datetime(6) NOT NULL,
  `apprenant_id` bigint NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  `reponse` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `avis_avis_apprenant_id_encadreur_id_a75341cd_uniq` (`apprenant_id`,`encadreur_id`),
  KEY `avis_avis_encadreur_id_5e7e8bbb_fk_utilisateurs_encadreur_id` (`encadreur_id`)
) ;

--
-- Déchargement des données de la table `avis_avis`
--

INSERT INTO `avis_avis` (`id`, `note`, `commentaire`, `date_creation`, `apprenant_id`, `encadreur_id`, `date_modification`, `reponse`) VALUES
(2, 2, 'good', '2026-03-27 18:05:56.179491', 5, 14, '2026-03-27 18:05:56.179533', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `catalogue_classe`
--

DROP TABLE IF EXISTS `catalogue_classe`;
CREATE TABLE IF NOT EXISTS `catalogue_classe` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordre` int UNSIGNED NOT NULL,
  `niveau_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `catalogue_classe_niveau_id_nom_e3cff7c0_uniq` (`niveau_id`,`nom`)
) ;

--
-- Déchargement des données de la table `catalogue_classe`
--

INSERT INTO `catalogue_classe` (`id`, `nom`, `ordre`, `niveau_id`) VALUES
(1, 'CP', 1, 1),
(2, 'CE1', 2, 1),
(3, 'CE2', 3, 1),
(4, 'CM1', 4, 1),
(5, 'CM2', 5, 1),
(6, '6ème', 1, 2),
(7, '5ème', 2, 2),
(8, '4ème', 3, 2),
(9, '3ème', 4, 2),
(10, '2nde', 1, 3);

-- --------------------------------------------------------

--
-- Structure de la table `catalogue_localisation`
--

DROP TABLE IF EXISTS `catalogue_localisation`;
CREATE TABLE IF NOT EXISTS `catalogue_localisation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ville` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quartier` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `catalogue_localisation_ville_quartier_65b9af02_uniq` (`ville`,`quartier`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `catalogue_localisation`
--

INSERT INTO `catalogue_localisation` (`id`, `ville`, `quartier`) VALUES
(5, 'Bobo-Dioulasso', 'Secteur 1'),
(6, 'Bobo-Dioulasso', 'Secteur 2'),
(7, 'Bobo-Dioulasso', 'Secteur 3'),
(8, 'Koudougou', 'Centre'),
(9, 'Koudougou', 'Nabonswendé'),
(1, 'Ouagadougou', 'Dapoya'),
(4, 'Ouagadougou', 'Gounghin'),
(3, 'Ouagadougou', 'Koulouba'),
(2, 'Ouagadougou', 'Patte d\'oie');

-- --------------------------------------------------------

--
-- Structure de la table `catalogue_matiere`
--

DROP TABLE IF EXISTS `catalogue_matiere`;
CREATE TABLE IF NOT EXISTS `catalogue_matiere` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `catalogue_matiere`
--

INSERT INTO `catalogue_matiere` (`id`, `nom`) VALUES
(4, 'Anglais'),
(8, 'Espagnol'),
(2, 'Français'),
(5, 'Histoire-Géographie'),
(1, 'Mathématiques'),
(7, 'Philosophie'),
(3, 'Physique-Chimie'),
(6, 'SVT');

-- --------------------------------------------------------

--
-- Structure de la table `catalogue_niveau`
--

DROP TABLE IF EXISTS `catalogue_niveau`;
CREATE TABLE IF NOT EXISTS `catalogue_niveau` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `catalogue_niveau`
--

INSERT INTO `catalogue_niveau` (`id`, `nom`) VALUES
(2, 'Collège (6ème - 3ème)'),
(3, 'Lycée (Seconde - Terminale)'),
(1, 'Primaire');

-- --------------------------------------------------------

--
-- Structure de la table `cours_demandecours`
--

DROP TABLE IF EXISTS `cours_demandecours`;
CREATE TABLE IF NOT EXISTS `cours_demandecours` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `disponibilites` longtext COLLATE utf8mb4_unicode_ci,
  `localite` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `message` longtext COLLATE utf8mb4_unicode_ci,
  `date_proposee` datetime(6) DEFAULT NULL,
  `duree_proposee` int UNSIGNED DEFAULT NULL,
  `lieu_cours` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tarif_propose` decimal(8,2) DEFAULT NULL,
  `statut` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_demande` datetime(6) NOT NULL,
  `apprenant_id` bigint NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `enfant_id` bigint DEFAULT NULL,
  `matiere_id` bigint NOT NULL,
  `niveau_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cours_demandecours_apprenant_id_61b53423_fk_utilisate` (`apprenant_id`),
  KEY `cours_demandecours_encadreur_id_f4dd8fb8_fk_utilisate` (`encadreur_id`),
  KEY `cours_demandecours_enfant_id_10f31c3c_fk_utilisateurs_enfant_id` (`enfant_id`),
  KEY `cours_demandecours_matiere_id_53ecaf0c_fk_catalogue_matiere_id` (`matiere_id`),
  KEY `cours_demandecours_niveau_id_cfc19cb1_fk_catalogue_niveau_id` (`niveau_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_utilisateurs_utilisateur_id` (`user_id`)
) ;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-03-23 11:11:52.069963', '6', 'prof1 - Mathématiques (Lycée (Seconde - Terminale)) - Série D - Ouagadougou - Dapoya', 1, '[{\"added\": {}}]', 15, 1),
(2, '2026-03-23 11:12:23.031437', '7', 'prof1 - SVT (Lycée (Seconde - Terminale)) - Série D - Ouagadougou - Dapoya', 1, '[{\"added\": {}}]', 15, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(20, 'admin_app', 'abonnementencadreur'),
(21, 'admin_app', 'documentencadreur'),
(22, 'admin_app', 'sanction'),
(23, 'admin_app', 'signalement'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(17, 'avis', 'avis'),
(27, 'catalogue', 'classe'),
(11, 'catalogue', 'localisation'),
(12, 'catalogue', 'matiere'),
(13, 'catalogue', 'niveau'),
(14, 'catalogue', 'serie'),
(15, 'catalogue', 'specialisation'),
(4, 'contenttypes', 'contenttype'),
(16, 'cours', 'demandecours'),
(18, 'messagerie', 'message'),
(19, 'messagerie', 'notification'),
(24, 'paiement', 'abonnement'),
(25, 'paiement', 'transaction'),
(5, 'sessions', 'session'),
(6, 'utilisateurs', 'apprenant'),
(7, 'utilisateurs', 'documentverification'),
(8, 'utilisateurs', 'encadreur'),
(9, 'utilisateurs', 'enfant'),
(28, 'utilisateurs', 'specialisation'),
(10, 'utilisateurs', 'utilisateur'),
(26, 'utilisateurs', 'verificationdocument');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-03-06 07:48:19.487401'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-03-06 07:48:20.996802'),
(3, 'auth', '0001_initial', '2026-03-06 07:48:25.359561'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-03-06 07:48:26.460344'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-03-06 07:48:26.503683'),
(6, 'auth', '0004_alter_user_username_opts', '2026-03-06 07:48:26.555906'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-03-06 07:48:26.636910'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-03-06 07:48:26.733760'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-03-06 07:48:26.817395'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-03-06 07:48:26.897028'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-03-06 07:48:26.976832'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-03-06 07:48:27.135993'),
(13, 'auth', '0011_update_proxy_permissions', '2026-03-06 07:48:27.183211'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-03-06 07:48:27.222080'),
(15, 'utilisateurs', '0001_initial', '2026-03-06 07:48:36.844326'),
(16, 'admin', '0001_initial', '2026-03-06 07:48:38.993838'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-03-06 07:48:39.053158'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-03-06 07:48:39.127707'),
(19, 'admin_app', '0001_initial', '2026-03-06 07:48:40.435506'),
(20, 'admin_app', '0002_initial', '2026-03-06 07:48:53.674912'),
(21, 'avis', '0001_initial', '2026-03-06 07:48:54.824465'),
(22, 'avis', '0002_initial', '2026-03-06 07:48:58.302009'),
(23, 'catalogue', '0001_initial', '2026-03-06 07:49:03.486160'),
(24, 'catalogue', '0002_initial', '2026-03-06 07:49:09.686701'),
(25, 'cours', '0001_initial', '2026-03-06 07:49:10.137038'),
(26, 'cours', '0002_initial', '2026-03-06 07:49:17.279253'),
(27, 'messagerie', '0001_initial', '2026-03-06 07:49:18.194844'),
(28, 'messagerie', '0002_initial', '2026-03-06 07:49:23.200703'),
(29, 'paiement', '0001_initial', '2026-03-06 07:49:24.147260'),
(30, 'paiement', '0002_initial', '2026-03-06 07:49:30.293755'),
(31, 'sessions', '0001_initial', '2026-03-06 07:49:31.548072'),
(32, 'avis', '0003_avis_date_modification_avis_reponse', '2026-03-06 14:00:54.822597'),
(33, 'utilisateurs', '0002_remove_encadreur_diplome_principal_and_more', '2026-03-09 14:11:07.865646'),
(34, 'utilisateurs', '0003_encadreur_bio_encadreur_date_inscription_and_more', '2026-03-18 03:29:04.685935'),
(35, 'admin_app', '0003_alter_documentencadreur_options_and_more', '2026-03-18 03:29:08.373231'),
(36, 'avis', '0004_alter_avis_options_alter_avis_note_and_more', '2026-03-18 03:29:09.158107'),
(37, 'catalogue', '0003_alter_localisation_options_alter_matiere_options_and_more', '2026-03-18 03:29:10.325820'),
(38, 'cours', '0003_alter_demandecours_options_and_more', '2026-03-18 03:29:10.651240'),
(39, 'messagerie', '0003_alter_message_options_alter_notification_options_and_more', '2026-03-18 03:29:13.372351'),
(40, 'utilisateurs', '0004_alter_apprenant_options_alter_encadreur_options_and_more', '2026-03-23 12:05:31.228883'),
(41, 'catalogue', '0004_specialisation_rayon_km_specialisation_se_deplace_and_more', '2026-03-23 12:05:39.344984'),
(42, 'admin_app', '0004_alter_documentencadreur_options_and_more', '2026-03-23 12:10:27.205909'),
(43, 'catalogue', '0005_specialisation_tarif_alter_specialisation_classe_and_more', '2026-03-23 13:27:39.672367'),
(44, 'utilisateurs', '0005_remove_encadreur_bio_remove_encadreur_description_and_more', '2026-03-23 13:27:42.093234'),
(45, 'cours', '0004_remove_demandecours_serie', '2026-03-25 12:20:29.094947'),
(46, 'catalogue', '0006_remove_specialisation_serie_and_more', '2026-03-25 12:20:34.231710'),
(47, 'utilisateurs', '0006_encadreur_rayon_km_encadreur_se_deplace', '2026-03-25 12:20:36.185297'),
(48, 'utilisateurs', '0007_alter_apprenant_options_alter_encadreur_options_and_more', '2026-03-26 14:52:24.895444'),
(49, 'catalogue', '0007_delete_specialisation', '2026-03-27 12:23:09.885580'),
(50, 'utilisateurs', '0008_specialisation', '2026-03-27 12:23:12.906106');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9cgftqaik2apnayg8p86gjo195t23ihn', '.eJxVjEEOwiAQAP_C2RDY7VLw6L1vaJaySNW0SWlPxr8bkh70OjOZtxr52Mt4VNnGOamrAqcuvzDy9JSlmfTg5b7qaV32bY66Jfq0VQ9rktftbP8GhWtpX8A-BoLOkheRQDFmBLJsoSeGbIwY9oENTeQzGhMdgg2MDtF2LqjPF-M1NqI:1w7KJa:2MUCnlRthLE_0FTn5MsNbCXWGgSHVI61EAlEOTvzsLE', '2026-04-13 21:38:30.358089'),
('aq1h212anih96c73rqq518q32h9rokyq', '.eJytjzFPwzAQhf-L5zhKAguZmgHBEpUFsSBFR3xJHByfazspUPW_c6ZCQmKtJ3_vPb27Owm0PSiPq-9CRCfqMhMD-aVTEEHUJ-E8WlpELWaarMjEBRQh_3EBbZgihrgbE-Q92xkLBt1EFtksLq9keUTrk_S4b9t75k0bk3j_3Dw0zIcVfNToWWLiyQFthKjJsgJf6OPnqukQ1DBO87s5fvSbzVISQjiSVyXHmp_Yrqxubv841X9nokid8zRo01lY0h6gKJ8djmwr7Qwt-OtUhXxdiwLvIjgM0tHqpbYhAh_gZZqQtg0SrTTUg5GwYS9fmvYpd2rgvt7qt-uVbVeqOp-_Aee3rYw:1w78gg:pbjDeaY_7pztGMJ7i_gHywGohQaMMa629dSP5UAl1qU', '2026-04-13 09:13:34.045520'),
('cc9lgbdqq2d6ay08157smkjptn0wl8d7', '.eJxVjEEOwiAQRe_C2hAQWsCl-56BzDCDVA1NSrsy3l1JutC__O_lvUSEfStxb7zGmcRFaHH6_RDSg2sHdId6W2Ra6rbOKLsiD9rktBA_r4f7FyjQSs9m8NpkhUpRQoXZsDHeQ9JjcCMCcTAuOKttdujI5mGwyKyBvnNnFO8P9QY4vA:1vyTvT:1_6ArhuK_kC6KVn2ye5m_q2wJNoTIBNI1BPUzfcyeCE', '2026-03-20 12:05:03.009415'),
('itx210ygpgjrluql28yone4pvjcv22rz', 'eyJlbmNhZHJldXJfc3RlcCI6MX0:1w78ht:YswnmEmRb6BZdUEh8Uwc_RUDisBYqExftLkMzJJ-DZA', '2026-04-13 09:14:49.356150'),
('kk864az93w9ql6mlystssemff6iqvdm6', 'eyJlbmNhZHJldXJfc3RlcCI6MX0:1w78hT:raVw-pLNafr_J0TPz9bOBpjVlVhHyw7zLXZ37syU738', '2026-04-13 09:14:23.478309'),
('onq1r2ctj1lij9yslju0stfed5wk2ur6', 'e30:1w6BbA:9WP6nK6YAJZRmaGfVwWRkO3NQNKsZAAaYPQbYJtqhP4', '2026-04-10 18:07:56.984475'),
('wpj4t9s3rztzr698cy9g8oqndanmjb4p', 'e30:1w78gy:KXeoeqGj02A2VAH5M0GICxlXn71W-o-Bm7RBCF0R--8', '2026-04-13 09:13:52.600465');

-- --------------------------------------------------------

--
-- Structure de la table `messagerie_message`
--

DROP TABLE IF EXISTS `messagerie_message`;
CREATE TABLE IF NOT EXISTS `messagerie_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contenu` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_envoi` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `destinataire_id` bigint NOT NULL,
  `expediteur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messagerie_message_destinataire_id_e5a9c7e9_fk_utilisate` (`destinataire_id`),
  KEY `messagerie_message_expediteur_id_9bb70195_fk_utilisate` (`expediteur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `messagerie_message`
--

INSERT INTO `messagerie_message` (`id`, `contenu`, `date_envoi`, `lu`, `destinataire_id`, `expediteur_id`) VALUES
(2, 'Bonjour, je souhaite vous contacter.', '2026-03-27 17:26:53.358456', 0, 14, 4),
(3, 'Bonjour, je souhaite vous contacter.', '2026-03-27 17:28:23.000242', 0, 14, 4),
(4, 'Bonjour, je souhaite vous contacter.', '2026-03-27 17:39:44.326465', 0, 14, 4),
(5, 'Bonjour, je souhaite vous contacter.', '2026-03-27 17:41:32.236665', 0, 14, 4),
(6, 'discutons sur', '2026-03-27 18:05:35.815750', 0, 18, 4),
(7, 'J\'aimerais en savoir plus sur...', '2026-03-30 13:33:47.274034', 0, 18, 15);

-- --------------------------------------------------------

--
-- Structure de la table `messagerie_notification`
--

DROP TABLE IF EXISTS `messagerie_notification`;
CREATE TABLE IF NOT EXISTS `messagerie_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_creation` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `message_id` bigint NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messagerie_notificat_message_id_7c948d0b_fk_messageri` (`message_id`),
  KEY `messagerie_notificat_utilisateur_id_68faa574_fk_utilisate` (`utilisateur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `messagerie_notification`
--

INSERT INTO `messagerie_notification` (`id`, `date_creation`, `lu`, `message_id`, `utilisateur_id`) VALUES
(1, '2026-03-27 17:26:53.499673', 0, 2, 14),
(2, '2026-03-27 17:28:23.157536', 0, 3, 14),
(3, '2026-03-27 17:39:44.451381', 0, 4, 14),
(4, '2026-03-27 17:41:32.367401', 0, 5, 14),
(5, '2026-03-27 18:05:35.906287', 0, 6, 18),
(6, '2026-03-30 13:33:47.873514', 0, 7, 18);

-- --------------------------------------------------------

--
-- Structure de la table `paiement_abonnement`
--

DROP TABLE IF EXISTS `paiement_abonnement`;
CREATE TABLE IF NOT EXISTS `paiement_abonnement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_debut` datetime(6) NOT NULL,
  `date_expiration` datetime(6) NOT NULL,
  `actif` tinyint(1) NOT NULL,
  `periode_essai` tinyint(1) NOT NULL,
  `encadreur_id` bigint NOT NULL,
  `transaction_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `paiement_abonnement_encadreur_id_875c6f53_fk_utilisate` (`encadreur_id`),
  KEY `paiement_abonnement_transaction_id_7933d64e_fk_paiement_` (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `paiement_transaction`
--

DROP TABLE IF EXISTS `paiement_transaction`;
CREATE TABLE IF NOT EXISTS `paiement_transaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `montant` decimal(10,2) NOT NULL,
  `devise` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_paiement` datetime(6) NOT NULL,
  `statut` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `reference` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `encadreur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reference` (`reference`),
  KEY `paiement_transaction_encadreur_id_fcd242b4_fk_utilisate` (`encadreur_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_apprenant`
--

DROP TABLE IF EXISTS `utilisateurs_apprenant`;
CREATE TABLE IF NOT EXISTS `utilisateurs_apprenant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `niveau_scolaire` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `type_apprenant` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateur_id` (`utilisateur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `utilisateurs_apprenant`
--

INSERT INTO `utilisateurs_apprenant` (`id`, `utilisateur_id`, `niveau_scolaire`, `type_apprenant`) VALUES
(1, 2, NULL, 'ELEVE'),
(5, 4, '', 'PARENT'),
(6, 5, '', 'ELEVE'),
(7, 6, '', 'ELEVE'),
(9, 8, '', 'PARENT'),
(11, 10, '', 'ELEVE'),
(12, 11, '', 'PARENT'),
(13, 12, '', 'ELEVE'),
(15, 14, '', 'ELEVE'),
(16, 15, '', 'ELEVE'),
(17, 16, '', 'PARENT'),
(18, 17, '', 'PARENT');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_encadreur`
--

DROP TABLE IF EXISTS `utilisateurs_encadreur`;
CREATE TABLE IF NOT EXISTS `utilisateurs_encadreur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `genre` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_inscription` datetime(6) NOT NULL,
  `nb_evaluations` int DEFAULT '0',
  `note_moyenne` float DEFAULT '0',
  `quartier` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ville` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `presentation` text COLLATE utf8mb4_unicode_ci,
  `rayon_km` int DEFAULT '10',
  `se_deplace` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateur_id` (`utilisateur_id`)
) ;

--
-- Déchargement des données de la table `utilisateurs_encadreur`
--

INSERT INTO `utilisateurs_encadreur` (`id`, `utilisateur_id`, `genre`, `date_inscription`, `nb_evaluations`, `note_moyenne`, `quartier`, `ville`, `presentation`, `rayon_km`, `se_deplace`) VALUES
(14, 18, 'FEMME', '2026-03-27 10:10:24.690201', 1, 2, '', 'KOUDOUGOU', 'ANNDDnui', 10, 1),
(15, 26, 'HOMME', '2026-03-30 21:38:23.260076', 0, 0, NULL, 'N', NULL, 10, 0);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_enfant`
--

DROP TABLE IF EXISTS `utilisateurs_enfant`;
CREATE TABLE IF NOT EXISTS `utilisateurs_enfant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `niveau_scolaire` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apprenant_id` bigint NOT NULL,
  `prenom` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateurs_enfant_apprenant_id_17f407bc_fk_utilisate` (`apprenant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `utilisateurs_enfant`
--

INSERT INTO `utilisateurs_enfant` (`id`, `nom`, `niveau_scolaire`, `apprenant_id`, `prenom`) VALUES
(1, 'Ouédraogo', '3ème', 1, 'Saidou'),
(2, 'Ouédraogo', '6ème', 1, 'Aïssata'),
(3, 'LOMPO', '6ème', 5, 'Déborah'),
(4, 'LOMPO', 'Première', 5, 'Israel'),
(8, 'LOMPO', '3ème', 5, 'Samuel');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_specialisation`
--

DROP TABLE IF EXISTS `utilisateurs_specialisation`;
CREATE TABLE IF NOT EXISTS `utilisateurs_specialisation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tarif` int NOT NULL,
  `type_cours` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `classe_id` bigint DEFAULT NULL,
  `encadreur_id` bigint NOT NULL,
  `matiere_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateurs_special_classe_id_fb4e6536_fk_catalogue` (`classe_id`),
  KEY `utilisateurs_special_encadreur_id_9113de44_fk_utilisate` (`encadreur_id`),
  KEY `utilisateurs_special_matiere_id_1a8878a2_fk_catalogue` (`matiere_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `utilisateurs_specialisation`
--

INSERT INTO `utilisateurs_specialisation` (`id`, `tarif`, `type_cours`, `classe_id`, `encadreur_id`, `matiere_id`) VALUES
(1, 2500, 'DOMICILE', 9, 14, 1),
(2, 5000, 'GROUPE', 8, 14, 3);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_utilisateur`
--

DROP TABLE IF EXISTS `utilisateurs_utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateurs_utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `est_verifie` tinyint(1) NOT NULL,
  `photo_profil` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telephone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date_inscription` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `utilisateurs_utilisateur_email_d1f98970_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `utilisateurs_utilisateur`
--

INSERT INTO `utilisateurs_utilisateur` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`, `est_verifie`, `photo_profil`, `telephone`, `date_inscription`) VALUES
(1, 'pbkdf2_sha256$1200000$pFwricK2Ld8WgC4HPJgjLy$Z8/+P4J1GnfZxNEdIJWyD3On+aZUI3ghRwuWg8AZJ5E=', '2026-03-30 11:36:16.871451', 1, 'Nethania', '', '', 'compaoreconstance2@gmail.com', 1, 1, '2026-03-06 10:27:20.507130', '', 0, NULL, NULL, '2026-03-18 03:29:03.148221'),
(2, 'pbkdf2_sha256$1200000$0LS7mgrVgSaERfhzftZVLe$pAzjAoKGEibtVO1Yo2vhQoKB1uDMsrpN/KiPt80uIOQ=', NULL, 0, 'eleve1', '', '', '', 0, 1, '2026-03-07 11:40:26.971576', 'APPRENANT', 0, NULL, NULL, '2026-03-18 03:29:03.148221'),
(4, 'pbkdf2_sha256$1200000$gncpXn7MFsHb3xCCKdc1xP$2HeK40oqvQpV36QF6z/HYKa7fDZLuY7qfHwWdd8ezWo=', '2026-03-30 09:14:23.765080', 0, 'G', 'lina', 'ko', 'liko@gmail.com', 0, 1, '2026-03-24 23:39:32.083584', 'APPRENANT', 0, 'profils/eleves-apprenant-ecole-dans-leur-classe_23-2149511026.avif', '12345678', '2026-03-24 23:39:36.378502'),
(5, 'pbkdf2_sha256$1200000$J5vebyDOiQx9TfHulLGf3H$z+R/Jm5EZcBWbPIZzg/mGeEueYZ6t6qfM8HQq7Ca368=', '2026-03-27 13:26:10.281485', 0, 'ami', '', '', 'ami@gmail.com', 0, 1, '2026-03-25 00:21:09.705909', 'APPRENANT', 0, '', '12345678', '2026-03-25 00:21:14.280691'),
(6, 'pbkdf2_sha256$1200000$uX6rw2ZY4xs2oGBQoEWFTJ$2G5Guq3OJs89oKc9qt7AO1ZvnkLsL4e1b3le4QvfLmQ=', '2026-03-25 15:24:34.426797', 0, 'mom', '', '', 'mom@gmail.com', 0, 1, '2026-03-25 15:23:56.046124', 'APPRENANT', 0, '', '+226  74 32 91 03', '2026-03-25 15:24:01.215213'),
(8, 'pbkdf2_sha256$1200000$ID9t2yyF1Lbed6MWw13ZE7$KsMGkbFaqmH5DbHTogV7gxZOXpkEM0Tcwa400d0Pel0=', '2026-03-26 15:11:33.422247', 0, 'oubda_sala', 'sala', 'Oubda', 'sal23@gmail.com', 0, 1, '2026-03-26 11:41:53.035279', 'APPRENANT', 0, '', '64523890', '2026-03-26 11:41:57.824364'),
(10, 'pbkdf2_sha256$1200000$JZiZ6m4q56tci2cvIEJe0N$tT6xef2ShPucZUjRm+FsEbAPg4zF4EMNsS7cc71Yq3U=', '2026-03-26 13:17:41.490888', 0, 'ouedraogo_issa', 'issa', 'Ouedraogo', 'issa@gmail.com', 0, 1, '2026-03-26 13:17:36.890543', 'APPRENANT', 0, '', '63546789', '2026-03-26 13:17:40.763890'),
(11, 'pbkdf2_sha256$1200000$0zrCTYPHZt4FTEhSogjxGA$3VuOEccNjb94W3mX/IELEVaGdU8ujDiwR4nXyAddCiE=', '2026-03-27 11:31:46.671184', 0, 'ada.kindo', 'Ada', 'kindo', 'aki7@gmail.com', 0, 1, '2026-03-26 14:16:40.095427', 'APPRENANT', 0, '', '76549809', '2026-03-26 14:16:44.489952'),
(12, 'pbkdf2_sha256$1200000$kKTNHviDLh0nE3LsBjl6R8$CFKam58QNa2UAfjjUlmLoPnlckF8GzbNmXNg3v0YcmE=', '2026-03-27 11:33:13.139689', 0, 'marcela.soré', 'marcela', 'Soré', 'maso@gmail.com', 0, 1, '2026-03-26 14:18:27.121797', 'APPRENANT', 0, '', '76549809', '2026-03-26 14:18:30.892896'),
(14, 'pbkdf2_sha256$1200000$eHrDCGtvovFK2n14V8s471$UEDptg1pP+woFB/n7TQ/YQC67MhP0uEfL0/wFJ+CMH4=', '2026-03-26 16:01:08.890075', 0, 'test.test', 'test', 'test', 'test@gmail.com', 0, 1, '2026-03-26 16:01:03.639351', 'APPRENANT', 0, '', '45678990', '2026-03-26 16:01:08.501904'),
(15, 'pbkdf2_sha256$1200000$UGcvOL9Jz9t3JR5w9Uyvou$4pVBpRAFdrwaOAM8djOWAWvCelth7aWfmBTbyYPlEH0=', '2026-03-30 12:22:55.904934', 0, 'béni.diallo', 'Béni', 'DIALLO', 'belo@gmail.com', 0, 1, '2026-03-26 16:25:50.713367', 'APPRENANT', 0, '', '64687543', '2026-03-26 16:25:55.188970'),
(16, 'pbkdf2_sha256$1200000$G14tSFm38fkfoaAog0Tnwv$XAGZ/+yLvxEtXWBJSXlXeCJtUG4V4/LB4iA7xXv/r98=', '2026-03-26 16:29:43.042536', 0, 'cojo.colo', 'cojo', 'colo', 'joco@gmail.com', 0, 1, '2026-03-26 16:29:38.822583', 'APPRENANT', 0, '', '27872398', '2026-03-26 16:29:42.667109'),
(17, 'pbkdf2_sha256$1200000$Yx5iRr5PUhayhAbS5fvNix$v0UWuCbELh++jSlZWIiAtLGOIY54vEcf+VrxP/jEzLU=', '2026-03-30 19:35:06.389063', 0, 'bintou.barry', 'bintou', 'BARRY', 'bb@gmail.com', 0, 1, '2026-03-26 16:54:29.420251', 'APPRENANT', 0, '', '32455677', '2026-03-26 16:54:33.969821'),
(18, 'pbkdf2_sha256$1200000$G1O5FG9ZoMnSQJ9M5G8O38$bPxKTg0ByDXQ1nIpxw4Cbvfofp80ZKTAiCvvpnOKfOU=', '2026-03-30 13:34:26.400317', 0, 'madina.soro', 'madina', 'soro', 'madiso@gmail.com', 0, 1, '2026-03-27 10:10:17.350971', 'ENCADREUR', 1, 'profils/bannière.jpeg', '45678900', '2026-03-27 10:10:24.567348'),
(19, 'pbkdf2_sha256$1200000$BHvtXx7Cq3C1oSmVT1iLY3$22Ud6XRGqFl0gZNUmlGXdXtznsm/RBhDnFF2v+cvK44=', NULL, 0, 'john.doe', 'john', 'doe', 'test2@gmail.com', 0, 1, '2026-03-30 09:12:06.457196', 'ENCADREUR', 0, 'profils/ado.jpeg', '00000001', '2026-03-30 09:12:09.914654'),
(20, 'pbkdf2_sha256$1200000$iJkStsCXAHr7mFUVy9o1ny$hLHLkwXUoe/qEAcr5acPFKHGELJwwXqmTRROcxgTIR4=', NULL, 0, 'constance.compaore', 'constance', 'Compaore', 'coco@gmail.com', 0, 1, '2026-03-30 16:20:48.256919', 'ENCADREUR', 0, '', '76546789', '2026-03-30 16:20:52.357604'),
(21, 'pbkdf2_sha256$1200000$sUXt8h6py3dhVL7oznKlaI$P0w7s81xzQIrUtpd6hIGZa9C77WMkFY45eqG24fHuow=', NULL, 0, 'constance.compaore1', 'constance', 'Compaore', 'cococo@gmail.com', 0, 1, '2026-03-30 16:23:08.147518', 'ENCADREUR', 0, '', '76546789', '2026-03-30 16:23:11.488424'),
(22, 'pbkdf2_sha256$1200000$ujEiB7x8kRFNWJtXnms600$R9DIsW5aEf1h2Jwvpfi1AuNDxwIn6BjduYRgjgWr1G4=', NULL, 0, 'isaac.kossi', 'isaac', 'kossi', 'iko@gmail.com', 0, 1, '2026-03-30 19:14:52.881929', 'ENCADREUR', 0, '', '12345666', '2026-03-30 19:14:56.141219'),
(26, 'pbkdf2_sha256$1200000$cLu0Yrxtws1LQ4uAfmgXN1$znhUDkbaA8obbekSY9Hbg9b/d3ZOSizifqzQPqo3sL4=', '2026-03-30 21:38:30.111845', 0, 'n.n', 'n', 'n', 'nad@gmail.com', 0, 1, '2026-03-30 21:38:19.584804', 'ENCADREUR', 0, '', '43536477', '2026-03-30 21:38:23.032493');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_utilisateur_groups`
--

DROP TABLE IF EXISTS `utilisateurs_utilisateur_groups`;
CREATE TABLE IF NOT EXISTS `utilisateurs_utilisateur_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateurs_utilisateur_utilisateur_id_group_id_954b1d5c_uniq` (`utilisateur_id`,`group_id`),
  KEY `utilisateurs_utilisa_group_id_9cd3c896_fk_auth_grou` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_utilisateur_user_permissions`
--

DROP TABLE IF EXISTS `utilisateurs_utilisateur_user_permissions`;
CREATE TABLE IF NOT EXISTS `utilisateurs_utilisateur_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `utilisateurs_utilisateur_utilisateur_id_permissio_a16db5bb_uniq` (`utilisateur_id`,`permission_id`),
  KEY `utilisateurs_utilisa_permission_id_42b32d4e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs_verificationdocument`
--

DROP TABLE IF EXISTS `utilisateurs_verificationdocument`;
CREATE TABLE IF NOT EXISTS `utilisateurs_verificationdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type_document` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fichier` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `statut` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_verification` datetime(6) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `commentaire_admin` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateurs_verific_utilisateur_id_57fcd7ef_fk_utilisate` (`utilisateur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `utilisateurs_verificationdocument`
--

INSERT INTO `utilisateurs_verificationdocument` (`id`, `type_document`, `fichier`, `statut`, `date_verification`, `utilisateur_id`, `commentaire_admin`) VALUES
(1, 'DIPLOME', 'documents/20-étapes-pour-installer-wordpress-en-local-avec-WAMP.pdf', 'EN_ATTENTE', '2026-03-27 10:10:24.918416', 18, ''),
(2, 'CNI', 'documents/ado.jpeg', 'EN_ATTENTE', '2026-03-27 10:10:25.011992', 18, ''),
(3, 'CV', 'documents/20-étapes-pour-installer-wordpress-en-local-avec-WAMP_7FEJeCT.pdf', 'EN_ATTENTE', '2026-03-27 10:10:25.179577', 18, ''),
(4, 'DIPLOME', 'documents/20-étapes-pour-installer-wordpress-en-local-avec-WAMP_KrWGv9b.pdf', 'EN_ATTENTE', '2026-03-30 21:38:27.535542', 26, ''),
(5, 'CNI', 'documents/20-étapes-pour-installer-wordpress-en-local-avec-WAMP_A3nZ1Vd.pdf', 'EN_ATTENTE', '2026-03-30 21:38:28.073368', 26, ''),
(6, 'CV', 'documents/20-étapes-pour-installer-wordpress-en-local-avec-WAMP_Y0RWX5t.pdf', 'EN_ATTENTE', '2026-03-30 21:38:28.683634', 26, '');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `admin_app_documentencadreur`
--
ALTER TABLE `admin_app_documentencadreur`
  ADD CONSTRAINT `admin_app_documenten_encadreur_id_d344314a_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`);

--
-- Contraintes pour la table `admin_app_sanction`
--
ALTER TABLE `admin_app_sanction`
  ADD CONSTRAINT `admin_app_sanction_encadreur_id_eae7655a_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`);

--
-- Contraintes pour la table `admin_app_signalement`
--
ALTER TABLE `admin_app_signalement`
  ADD CONSTRAINT `admin_app_signalemen_encadreur_id_ef58bfd2_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`),
  ADD CONSTRAINT `admin_app_signalemen_utilisateur_id_856f7a69_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `avis_avis`
--
ALTER TABLE `avis_avis`
  ADD CONSTRAINT `avis_avis_apprenant_id_0cb14fe4_fk_utilisateurs_apprenant_id` FOREIGN KEY (`apprenant_id`) REFERENCES `utilisateurs_apprenant` (`id`),
  ADD CONSTRAINT `avis_avis_encadreur_id_5e7e8bbb_fk_utilisateurs_encadreur_id` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`);

--
-- Contraintes pour la table `catalogue_classe`
--
ALTER TABLE `catalogue_classe`
  ADD CONSTRAINT `catalogue_classe_niveau_id_311b6c2e_fk_catalogue_niveau_id` FOREIGN KEY (`niveau_id`) REFERENCES `catalogue_niveau` (`id`);

--
-- Contraintes pour la table `cours_demandecours`
--
ALTER TABLE `cours_demandecours`
  ADD CONSTRAINT `cours_demandecours_apprenant_id_61b53423_fk_utilisate` FOREIGN KEY (`apprenant_id`) REFERENCES `utilisateurs_apprenant` (`id`),
  ADD CONSTRAINT `cours_demandecours_encadreur_id_f4dd8fb8_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`),
  ADD CONSTRAINT `cours_demandecours_enfant_id_10f31c3c_fk_utilisateurs_enfant_id` FOREIGN KEY (`enfant_id`) REFERENCES `utilisateurs_enfant` (`id`),
  ADD CONSTRAINT `cours_demandecours_matiere_id_53ecaf0c_fk_catalogue_matiere_id` FOREIGN KEY (`matiere_id`) REFERENCES `catalogue_matiere` (`id`),
  ADD CONSTRAINT `cours_demandecours_niveau_id_cfc19cb1_fk_catalogue_niveau_id` FOREIGN KEY (`niveau_id`) REFERENCES `catalogue_niveau` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_utilisateurs_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `messagerie_message`
--
ALTER TABLE `messagerie_message`
  ADD CONSTRAINT `messagerie_message_destinataire_id_e5a9c7e9_fk_utilisate` FOREIGN KEY (`destinataire_id`) REFERENCES `utilisateurs_utilisateur` (`id`),
  ADD CONSTRAINT `messagerie_message_expediteur_id_9bb70195_fk_utilisate` FOREIGN KEY (`expediteur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `messagerie_notification`
--
ALTER TABLE `messagerie_notification`
  ADD CONSTRAINT `messagerie_notificat_message_id_7c948d0b_fk_messageri` FOREIGN KEY (`message_id`) REFERENCES `messagerie_message` (`id`),
  ADD CONSTRAINT `messagerie_notificat_utilisateur_id_68faa574_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `paiement_abonnement`
--
ALTER TABLE `paiement_abonnement`
  ADD CONSTRAINT `paiement_abonnement_encadreur_id_875c6f53_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`),
  ADD CONSTRAINT `paiement_abonnement_transaction_id_7933d64e_fk_paiement_` FOREIGN KEY (`transaction_id`) REFERENCES `paiement_transaction` (`id`);

--
-- Contraintes pour la table `paiement_transaction`
--
ALTER TABLE `paiement_transaction`
  ADD CONSTRAINT `paiement_transaction_encadreur_id_fcd242b4_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`);

--
-- Contraintes pour la table `utilisateurs_apprenant`
--
ALTER TABLE `utilisateurs_apprenant`
  ADD CONSTRAINT `utilisateurs_apprena_utilisateur_id_9abbe29b_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `utilisateurs_encadreur`
--
ALTER TABLE `utilisateurs_encadreur`
  ADD CONSTRAINT `utilisateurs_encadre_utilisateur_id_9c2b347e_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `utilisateurs_enfant`
--
ALTER TABLE `utilisateurs_enfant`
  ADD CONSTRAINT `utilisateurs_enfant_apprenant_id_17f407bc_fk_utilisate` FOREIGN KEY (`apprenant_id`) REFERENCES `utilisateurs_apprenant` (`id`);

--
-- Contraintes pour la table `utilisateurs_specialisation`
--
ALTER TABLE `utilisateurs_specialisation`
  ADD CONSTRAINT `utilisateurs_special_classe_id_fb4e6536_fk_catalogue` FOREIGN KEY (`classe_id`) REFERENCES `catalogue_classe` (`id`),
  ADD CONSTRAINT `utilisateurs_special_encadreur_id_9113de44_fk_utilisate` FOREIGN KEY (`encadreur_id`) REFERENCES `utilisateurs_encadreur` (`id`),
  ADD CONSTRAINT `utilisateurs_special_matiere_id_1a8878a2_fk_catalogue` FOREIGN KEY (`matiere_id`) REFERENCES `catalogue_matiere` (`id`);

--
-- Contraintes pour la table `utilisateurs_utilisateur_groups`
--
ALTER TABLE `utilisateurs_utilisateur_groups`
  ADD CONSTRAINT `utilisateurs_utilisa_group_id_9cd3c896_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `utilisateurs_utilisa_utilisateur_id_3264257e_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `utilisateurs_utilisateur_user_permissions`
--
ALTER TABLE `utilisateurs_utilisateur_user_permissions`
  ADD CONSTRAINT `utilisateurs_utilisa_permission_id_42b32d4e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `utilisateurs_utilisa_utilisateur_id_604dcf80_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);

--
-- Contraintes pour la table `utilisateurs_verificationdocument`
--
ALTER TABLE `utilisateurs_verificationdocument`
  ADD CONSTRAINT `utilisateurs_verific_utilisateur_id_57fcd7ef_fk_utilisate` FOREIGN KEY (`utilisateur_id`) REFERENCES `utilisateurs_utilisateur` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
