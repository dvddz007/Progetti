CREATE TABLE carte_d_identita(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  numero CHAR(9),
  firma VARCHAR(50),
  dtEmissione DATE,
  dtScadenza DATE
);

CREATE TABLE cittadini(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50),
  cognome VARCHAR(50),
  dtn DATE,
  cf CHAR(16),
  email VARCHAR(50),
  password VARCHAR(50)
);

CREATE TABLE t_sport(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

CREATE TABLE categorie(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

CREATE TABLE comuni(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50),
  km2 INT,
  n_abitanti INT
);

CREATE TABLE province(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

CREATE TABLE regioni(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

CREATE TABLE nazioni(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

CREATE TABLE continenti(
  pk INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50)
);

/*
ALTER TABLE carte_d_identita CHANGE daScadenza dtScadenza DATE;
ALTER TABLE carte_d_identita CHANGE numero numero CHAR(9);
ALTER TABLE comuni ADD COLUMN belfiore CHAR(4);
UPDATE carte_d_identita SET dtEmissione='2025-05-15' WHERE pk=1;
*/

INSERT INTO carte_d_identita(pk, numero, firma, dtEmissione, dtScadenza) VALUES (1, 'A1B2C3D4X', 'Davide Di Zio', '2025-05-15', '2029-02-03');
INSERT INTO carte_d_identita(numero, firma, dtEmissione, dtScadenza) VALUES ('A1B2C3D4Y', 'Mario Rossi', '2000-01-1', '2002-01-01');

INSERT INTO categorie(pk, nome) VALUES (1, 'Squadra');
INSERT INTO categorie(nome) VALUES ('Palla');

INSERT INTO cittadini(pk, nome, cognome, dtn, cf, email, password) VALUES (1, 'Davide', 'Di Zio', '2007-05-15', '', '', 'admin');
INSERT INTO cittadini(nome, cognome, dtn, cf, email, password) VALUES ('Mario', 'Rossi', '2000-01-01', 'ABCDEF01G23A001E', 'mario.rossi@gmail.com', 'password');

INSERT INTO comuni(pk, nome, km2, n_abitanti) VALUES (1, 'Atri', 1, 1);
INSERT INTO comuni(nome, km2, n_abitanti) VALUES ('Pescara', 1, 1);

INSERT INTO continenti(pk, nome) VALUES (1, 'Europa');
INSERT INTO continenti(nome) VALUES ('Asia');

INSERT INTO nazioni(pk, nome) VALUES (1, 'Italia');
INSERT INTO nazioni(nome) VALUES ('Germania');

INSERT INTO province(pk, nome) VALUES (1, 'Teramo');
INSERT INTO province(nome) VALUES ('Pescara');

INSERT INTO regioni(pk, nome) VALUES (1, 'Abruzzo');
INSERT INTO regioni(nome) VALUES ('Marche');

INSERT INTO t_sport(pk, nome) VALUES (1, 'Calcio');
INSERT INTO t_sport(nome) VALUES ('Tennis');

-- per i pk assenti:
/*
ALTER TABLE categorie ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE cittadini ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE comuni ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE continenti ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE nazioni ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE province ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE regioni ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE t_sport ADD COLUMN pk INT PRIMARY KEY AUTO_INCREMENT FIRST;
*/