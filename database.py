# import sqlite3


# conn = sqlite3.connect('school.db')

# cursor = conn.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students(
# id INTEGER PRIMARY KEY,
# name TEXT,
# age INTEGER

# )
# ''')

# cursor.execute('''
# INSERT INTO students(name, age)
# VALUES('princewill', 35)
# ''')
# conn.commit()



# students = [
#     ("john", 23),
#     ("JAME", 53),
#     ("Joel", 25)
# ]

# cursor.executemany('''
# INSERT INTO students(name, age)
# VALUES(?,?)
# ''', students)
# conn.commit()

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)


# cursor.execute('''
# UPDATE students
# SET age = 45
# WHERE id = 1
# ''')
# conn.commit()


# cursor.execute("""
# DELETE FROM students 
# WHERE id = 1
# """)
# conn.commit()





# cursor.execute("DROP TABLE students")
# conn.commit()

# conn.close();



import sqlite3

conn = sqlite3.connect('futurist.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS classes(
id  INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER ,
grad TEXT

)''')

cursor.execute('''
INSERT INTO classes(name, age, grad)
VALUES('joan', 23, 'ss1')
''')
conn.commit()



classes = [
    ("john", 23, "ss1"),
    ("JAME", 53, "ss2"),
    ("Joel", 25, "ss3")
]
cursor.executemany('''
INSERT INTO classes(name, age, grad)
VALUES(?,?,?)
''', classes)
conn.commit()


cursor.execute('''
UPDATE classes
SET grad = 'ss2'
WHERE id = 2
''')
conn.commit()


cursor.execute('''
DELETE FROM classes
WHERE id = 1
''')
conn.commit()


cursor.execute("SELECT * FROM classes")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()    