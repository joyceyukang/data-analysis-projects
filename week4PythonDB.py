import sqlite3

# connecting to sqlite
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object
cursor_obj = conn.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")
