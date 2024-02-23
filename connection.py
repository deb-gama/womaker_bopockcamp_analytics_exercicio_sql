import sqlite3

connection = sqlite3.connect('desafio_db.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

connection.commit()
connection.close()