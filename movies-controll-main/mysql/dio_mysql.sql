CREATE TABLE person (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT
    nome VARCHAR(30) NOT NULL
    nascimento DATE
);

INSERT INTO person (nome, nascimento) VALUES ('Eduardo', '1992-12-31');
INSERT INTO person (nome, nascimento) VALUES ('João', '1999-08-12');
INSERT INTO person (nome, nascimento) VALUES ('Maria', '2002-10-5');

UPDATE person SET nome='Eduardo Lauer' WHERE id=1;

DELETE FROM person WHERE id=1;

SELECT FROM person ORDER BY nome;
SELECT FROM person ORDER BY nome DESC;

ALTER TABLE erson ADD genero NOT NULL AFTER nascimento;

SELECT COUNT(genero), genero FROM person GROUP BY genero