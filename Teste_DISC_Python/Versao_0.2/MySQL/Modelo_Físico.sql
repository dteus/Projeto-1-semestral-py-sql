CREATE DATABASE auto_forms;
USE auto_forms;

CREATE TABLE `PERFIL` (
	`CPF` varchar(11) NOT NULL,
	`NOME` varchar(255),
	`EMAIL` varchar(255) NOT NULL,
	PRIMARY KEY (`CPF`)
);

CREATE TABLE `COLABORADORES` (
	`CRACHA` varchar(8) NOT NULL,
	`CPF` varchar(11) NOT NULL,
	`ID_SETOR` INT NOT NULL,
	`CARGO` varchar(255) NOT NULL,
	PRIMARY KEY (`CRACHA`)
);

CREATE TABLE `CURSO` (
	`ID_CURSO` INT NOT NULL AUTO_INCREMENT,
	`NOME_CURSO` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`ID_CURSO`)
);


CREATE TABLE `SETOR` (
	`ID_SETOR` INT NOT NULL AUTO_INCREMENT,
	`NOME_SETOR` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`ID_SETOR`)
);

CREATE TABLE `ALUNO` (
	`RA` varchar(8) NOT NULL,
	`CPF` varchar(11) NOT NULL,
	PRIMARY KEY (`RA`)
);

CREATE TABLE `Cursando` (
	`ID_TURMA` INT NOT NULL AUTO_INCREMENT,
	`ID_CURSO` INT NOT NULL,
	`RA` varchar(8) NOT NULL,
	PRIMARY KEY (`ID_TURMA`)
);

CREATE TABLE `HISTORICO_DISC` (
	`CPF` varchar(11) NOT NULL,
	`ID_PERGUNTA` INT NOT NULL,
	`RESPOSTA` varchar(255) NOT NULL,
	`ID_HISTORICO` INT NOT NULL AUTO_INCREMENT,
	`DATA` varchar(255) NOT NULL,
	PRIMARY KEY (`ID_HISTORICO`)
);

CREATE TABLE `PERGUNTA` (
	`ID_PERGUNTA` INT NOT NULL AUTO_INCREMENT,
	`PERGUNTA` varchar(500) NOT NULL,
	`NOME_TESTE` varchar(255) NOT NULL,
	PRIMARY KEY (`ID_PERGUNTA`)
);


CREATE TABLE `GABARITO` (
	`RESPOSTA` varchar(255) NOT NULL,
	`ID_PERGUNTA` INT NOT NULL,
	`CLASSIFICACAO` varchar(1) NOT NULL,
	PRIMARY KEY (`RESPOSTA`)
);

/*FALTA ADD CONSTRAINTS DELETE ON CASCADE*/

ALTER TABLE `COLABORADORES` ADD CONSTRAINT `COLABORADORES_fk0` FOREIGN KEY (`CPF`) REFERENCES `PERFIL`(`CPF`);

ALTER TABLE `ALUNO` ADD CONSTRAINT `ALUNO_fk0` FOREIGN KEY (`CPF`) REFERENCES `PERFIL`(`CPF`);

ALTER TABLE `Cursando` ADD CONSTRAINT `Cursando_fk0` FOREIGN KEY (`ID_CURSO`) REFERENCES `CURSO`(`ID_CURSO`);

ALTER TABLE `Cursando` ADD CONSTRAINT `Cursando_fk1` FOREIGN KEY (`RA`) REFERENCES `ALUNO`(`RA`);

ALTER TABLE `HISTORICO_DISC` ADD CONSTRAINT `HISTORICO_DISC_fk0` FOREIGN KEY (`CPF`) REFERENCES `ALUNO`(`CPF`);

ALTER TABLE `HISTORICO_DISC` ADD CONSTRAINT `HISTORICO_DISC_fk1` FOREIGN KEY (`ID_PERGUNTA`) REFERENCES `PERGUNTA`(`ID_PERGUNTA`);

ALTER TABLE `GABARITO` ADD CONSTRAINT `GABARITO_fk0` FOREIGN KEY (`ID_PERGUNTA`) REFERENCES `PERGUNTA`(`ID_PERGUNTA`);






















