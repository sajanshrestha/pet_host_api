import sqlite3

connection = sqlite3.connect('site.db')
cursor = connection.cursor()

query = 'CREATE TABLE IF NOT EXISTS owners (id INTEGER PRIMARY KEY, username VARCHAR(30), password VARCHAR(30))'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS hosts (id INTEGER PRIMARY KEY, username VARCHAR(30), password VARCHAR(30))'
cursor.execute(query)

connection.close()
