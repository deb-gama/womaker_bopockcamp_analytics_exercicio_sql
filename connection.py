import sqlite3

connection = sqlite3.connect('desafio_db.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "André Lima", 30, "Engenharia"), (2, "Maria José", 40, "Engenharia"), (3, "Rosa Almeida", 30, "Matemática"), (4, "Vitor Lima", 30, "Ed Física"), (1, "João Lima", 30, "Ed Física") ;')
cursor.execute('SELECT * from alunos;')
cursor.execute('SELECT * from alunos where idade > 20;')
cursor.execute('SELECT * curso = 'Engenharia' order by nome;')
cursor.execute('SELECT count(*) from alunos;')
cursor.execute('UPDATE alunos SET idade = 33 WHERE nome = 'André Lima';')
cursor.execute('DELETE FROM alunos WHERE id = 3;')


cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "André Lima", 30, 100.2), (2, "Maria José", 40, 500.25), (3, "Rosa Almeida", 30, 300.50), (4, "Vitor Lima", 30, 200.56), (5, "João Lima", 30, 100.10) ;')
cursor.execute('select nome, idade from clientes where idade > 30;')
cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1;')
cursor.execute('SELECT COUNT(*) from clientes where saldo > 1000;')


connection.commit()
connection.close()


