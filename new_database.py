import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS notes(
id  INTEGER PRIMARY KEY,
author TEXT NOT NULL,
age INTEGER ,
title TEXT
)''')

cursor.execute('''
INSERT INTO notes(author, title, age)
VALUES('Princewill', 'python', 2)
''')
conn.commit()

notes=[
    ('joel', 'html', 45),
    ('jame', 'css', 15),
    ('joan', 'javascript', 10),
]
cursor.executemany('''
INSERT INTO notes(author, title, age)
VALUES(?, ?, ?)
''', notes)
conn.commit()


cursor.execute('''
UPDATE notes
SET age = 20
WHERE id = 3
''')
conn.commit()

cursor.execute('''
DELETE FROM notes
WHERE id = 4
''')
conn.commit()

cursor.execute('SELECT * FROM notes')
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()
