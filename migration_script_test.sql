-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema multivender_test
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `multivender_test` ;

-- -----------------------------------------------------
-- Schema multivender_test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `multivender_test` DEFAULT CHARACTER SET latin1 ;
USE `multivender_test` ;

-- -----------------------------------------------------
-- Table `multivender_test`.`annotation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`annotation` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`annotation` (
  `anno_id` INT(11) NOT NULL,
  `annotator_id` VARCHAR(10) NULL DEFAULT NULL,
  `volume_id` VARCHAR(80) NOT NULL,
  `landmark_id` INT(11) NOT NULL,
  `world_x` FLOAT NULL DEFAULT NULL,
  `world_y` FLOAT NULL DEFAULT NULL,
  `world_z` FLOAT NULL DEFAULT NULL,
  `voxel_x` FLOAT NULL DEFAULT NULL,
  `voxel_y` FLOAT NULL DEFAULT NULL,
  `voxel_z` FLOAT NULL DEFAULT NULL,
  `rotate_angle` FLOAT NULL DEFAULT NULL,
  `confidence` FLOAT NULL DEFAULT NULL,
  `anno_time` DATETIME NULL,
  PRIMARY KEY (`anno_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`case_monitor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`case_monitor` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`case_monitor` (
  `volume_id` VARCHAR(80) NOT NULL,
  `in_memory` TINYINT(1) NULL DEFAULT NULL,
  `on_disk` TINYINT(1) NULL DEFAULT NULL,
  `is_locked` TINYINT(1) NULL DEFAULT NULL,
  `num_loaded` INT(11) NULL DEFAULT NULL,
  `last_accessed` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_dicominfo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_dicominfo` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_dicominfo` (
  `volume_id` VARCHAR(80) NOT NULL,
  `dicom_path` VARCHAR(256) NULL DEFAULT NULL,
  `series` TINYINT(1) NULL DEFAULT NULL,
  `SeriesDescription` VARCHAR(64) NULL DEFAULT NULL,
  `PatientsName` VARCHAR(80) NULL DEFAULT NULL,
  `PatientsAge` INT(4) NULL DEFAULT NULL,
  `PatientsSex` VARCHAR(8) NULL DEFAULT NULL,
  `Modality` VARCHAR(10) NULL DEFAULT NULL,
  `BodyPartExamined` VARCHAR(16) NULL DEFAULT NULL,
  `Manufacturer` VARCHAR(32) NULL DEFAULT NULL,
  `ProtocolName` VARCHAR(64) NULL DEFAULT NULL,
  `StudyDescription` VARCHAR(64) NULL DEFAULT NULL,
  `StudyInstanceUID` VARCHAR(64) NULL DEFAULT NULL,
  `FrameOfReferenceUID` VARCHAR(80) NULL DEFAULT NULL,
  `RequestedProcedureDescription` VARCHAR(64) NULL DEFAULT NULL,
  `PixelSpacing` VARCHAR(64) NULL DEFAULT NULL,
  `ImageOrientationPatient` VARCHAR(144) NULL DEFAULT NULL,
  `PatientPosition` VARCHAR(64) NULL DEFAULT NULL,
  `SliceThickness` FLOAT NULL DEFAULT NULL,
  `ConvolutionKernel` VARCHAR(64) NULL DEFAULT NULL,
  `PhotometricInterpretation` VARCHAR(32) NULL DEFAULT NULL,
  `WindowCenter` VARCHAR(64) NULL DEFAULT NULL,
  `WindowWidth` VARCHAR(64) NULL DEFAULT NULL,
  `ImageType` VARCHAR(128) NULL DEFAULT NULL,
  `ImageComments` VARCHAR(128) NULL DEFAULT NULL,
  `num_slices` INT(11) NULL DEFAULT NULL,
  `width` INT(11) NULL DEFAULT NULL,
  `height` INT(11) NULL DEFAULT NULL,
  `depth` INT(11) NULL DEFAULT NULL,
  `x_min` FLOAT NULL DEFAULT NULL,
  `y_min` FLOAT NULL DEFAULT NULL,
  `z_min` FLOAT NULL DEFAULT NULL,
  `x_max` FLOAT NULL DEFAULT NULL,
  `y_max` FLOAT NULL DEFAULT NULL,
  `z_max` FLOAT NULL DEFAULT NULL,
  `origin_x` FLOAT NULL DEFAULT NULL,
  `origin_y` FLOAT NULL DEFAULT NULL,
  `origin_z` FLOAT NULL DEFAULT NULL,
  `space_x` FLOAT NULL DEFAULT NULL,
  `space_y` FLOAT NULL DEFAULT NULL,
  `space_z` FLOAT NULL DEFAULT NULL,
  `orientation` VARCHAR(3) NULL DEFAULT NULL,
  `box_str` VARCHAR(256) NULL DEFAULT NULL,
  `last_accessed` DATETIME NULL DEFAULT NULL,
  `comment` VARCHAR(128) NULL DEFAULT NULL,
  `MagneticFieldStrength` FLOAT NULL DEFAULT NULL,
  `FlipAngle` FLOAT NULL DEFAULT NULL,
  `RepetitionTime` FLOAT NULL DEFAULT NULL,
  `EchoTime` FLOAT NULL DEFAULT NULL,
  `ImagingFrequency` FLOAT NULL DEFAULT NULL,
  `EchoTrainLength` FLOAT NULL DEFAULT NULL,
  `SequenceName` VARCHAR(255) NULL DEFAULT NULL,
  `ImagedNucleus` VARCHAR(255) NULL DEFAULT NULL,
  `TransmitCoilName` VARCHAR(255) NULL DEFAULT NULL,
  `InversionTime` VARCHAR(64) NULL DEFAULT NULL,
  `ScanningSequence` VARCHAR(128) NULL DEFAULT NULL,
  `CoilList` VARCHAR(512) NULL DEFAULT NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`detection`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`detection` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`detection` (
  `detection_id` INT(11) NOT NULL,
  `volume_id` VARCHAR(80) NOT NULL,
  `landmark_id` INT(11) NOT NULL,
  `world_x` FLOAT NULL DEFAULT NULL,
  `world_y` FLOAT NULL DEFAULT NULL,
  `world_z` FLOAT NULL DEFAULT NULL,
  `voxel_x` FLOAT NULL DEFAULT NULL,
  `voxel_y` FLOAT NULL DEFAULT NULL,
  `voxel_z` FLOAT NULL DEFAULT NULL,
  `confidence` FLOAT NULL DEFAULT NULL,
  `detection_time` DATETIME NULL,
  PRIMARY KEY (`detection_id`),
  CONSTRAINT `volume_id`
    FOREIGN KEY (`volume_id`)
    REFERENCES `multivender_test`.`volume_dicominfo` (`volume_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

CREATE INDEX `volume_id_idx` ON `multivender_test`.`detection` (`volume_id` ASC);


-- -----------------------------------------------------
-- Table `multivender_test`.`mapped_drives`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`mapped_drives` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`mapped_drives` (
  `drive_id` INT(11) NOT NULL,
  `drive_name` VARCHAR(10) NULL DEFAULT NULL,
  `real_path` VARCHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`drive_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`pure_negative`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`pure_negative` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`pure_negative` (
  `pureneg_id` INT(11) NOT NULL,
  `annotator_id` LONGTEXT NULL DEFAULT NULL,
  `landmark_id` INT(11) NOT NULL,
  `volume_id` VARCHAR(80) NOT NULL,
  `anno_time` DATETIME NULL,
  PRIMARY KEY (`pureneg_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_bodypart`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_bodypart` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_bodypart` (
  `volume_id` VARCHAR(80) NOT NULL,
  `start_slice` INT(11) NULL DEFAULT NULL,
  `end_slice` INT(11) NULL DEFAULT NULL,
  `tag_time` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_contrast`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_contrast` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_contrast` (
  `volume_id` VARCHAR(80) NOT NULL,
  `pulmonary_trunk` INT(11) NULL DEFAULT NULL,
  `aortic_arch` INT(11) NULL DEFAULT NULL,
  `ascending_aorta` INT(11) NULL DEFAULT NULL,
  `descending_aorta` INT(11) NULL DEFAULT NULL,
  `carotid_arteries` INT(11) NULL DEFAULT NULL,
  `iliac_bifurcation` INT(11) NULL DEFAULT NULL,
  `LV_of_heart` INT(11) NULL DEFAULT NULL,
  `coronary_LM` INT(11) NULL DEFAULT NULL,
  `coronary_RCA` INT(11) NULL DEFAULT NULL,
  `tag_time` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_filelist`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_filelist` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_filelist` (
  `volume_id` VARCHAR(80) NOT NULL,
  `filelist` LONGBLOB NULL DEFAULT NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_mpr`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_mpr` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_mpr` (
  `volume_id` VARCHAR(80) NOT NULL,
  `axial` LONGBLOB NULL DEFAULT NULL,
  `coronal` LONGBLOB NULL DEFAULT NULL,
  `sagittal` LONGBLOB NULL DEFAULT NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_spine`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_spine` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_spine` (
  `volume_id` VARCHAR(80) NOT NULL,
  `cpr` LONGBLOB NULL DEFAULT NULL,
  `class_id` INT(11) NULL DEFAULT NULL,
  `tag_time` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_tag` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_tag` (
  `volume_id` VARCHAR(80) NOT NULL,
  `tag_result` VARCHAR(128) NULL DEFAULT NULL,
  `tag_time` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `multivender_test`.`volume_xr_view`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `multivender_test`.`volume_xr_view` ;

CREATE TABLE IF NOT EXISTS `multivender_test`.`volume_xr_view` (
  `volume_id` VARCHAR(80) NOT NULL,
  `view_type` INT(11) NULL DEFAULT NULL,
  `tag_time` DATETIME NULL,
  PRIMARY KEY (`volume_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
