import sqlite3

conn = sqlite3.connect('futurelabs.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT,
    age     INTEGER,
    course  TEXT,
    email   TEXT
)
''')
conn.commit()

def add_student():

    name   = input("Name   : ")

    cursor.execute("SELECT name FROM students WHERE name = ?", (name,))
    existing_student = cursor.fetchone()

    if existing_student:
        print(f"\n❌ Error: The student '{name}' already exists in the database!")
        return;

    age    = input("Age    : ")
    course = input("Course : ")
    email  = input("Email  : ")

    cursor.execute('''
    INSERT INTO students (name, age, course, email)
    VALUES (?, ?, ?, ?)
    ''', (name, age, course, email))
    conn.commit()
    print("Student added!")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def search_student():
    search_name = input("Enter name to search: ")
    
    cursor.execute("SELECT * FROM students WHERE name = ?", (search_name,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print(f"❌ Notice: The name '{search_name}' does not exist in the database.")

  


def update_student():
    student_id = input("Enter student ID to update: ")
    new_course = input("Enter new course: ")

    cursor.execute('''
    UPDATE students
    SET course = ?
    WHERE id = ?
    ''', (new_course, student_id))
    conn.commit()
    print("Student updated!")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    cursor.execute('''
    DELETE FROM students
    WHERE id = ?
    ''', (student_id,))
    conn.commit()
    print("Student deleted!")


def export_report():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    with open("student_report.txt", "w") as file:
        for row in rows:
            file.write(str(row) + "\n")

    print("Report saved to student_report.txt!")

while True:
    print("\n=========================")
    print(" STUDENT REGISTRATION SYSTEM")
    print("=========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Export Report")
    print("7. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        export_report()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")


conn.close()