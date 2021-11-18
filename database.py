import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""

cursor.execute(command)

cursor.execute("INSERT INTO users VALUES ('pravin', '1234')")
cursor.execute("INSERT INTO users VALUES ('jean', '5678')")
cursor.execute("INSERT INTO users VALUES ('admin', 'orange')")

connection.commit()