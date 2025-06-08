import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root'
)

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE elderco')

print('database created')