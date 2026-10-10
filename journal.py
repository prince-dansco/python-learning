# import sqlite3
# import os
# from datetime import datetime


# # ─────────────────────────────────────────
# #  DATABASE SETUP
# # ─────────────────────────────────────────

# def connect():
#     return sqlite3.connect("students.db")


# def create_table():
#     with connect() as conn:
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS students (
#                 id      INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name    TEXT    NOT NULL,
#                 age     INTEGER NOT NULL,
#                 course  TEXT    NOT NULL,
#                 email   TEXT    NOT NULL UNIQUE
#             )
#         """)


# # ─────────────────────────────────────────
# #  HELPERS
# # ─────────────────────────────────────────

# def clear():
#     os.system("cls" if os.name == "nt" else "clear")


# def header(title="STUDENT REGISTRATION SYSTEM"):
#     print("\n" + "=" * 35)
#     print(f"  {title}")
#     print("=" * 35)


# def pause():
#     input("\nPress Enter to continue...")


# def print_table(rows):
#     if not rows:
#         print("\n  No records found.")
#         return

#     print(f"\n{'ID':<6} {'Name':<20} {'Age':<5} {'Course':<20} {'Email'}")
#     print("-" * 75)
#     for r in rows:
#         print(f"{r[0]:<6} {r[1]:<20} {r[2]:<5} {r[3]:<20} {r[4]}")


# # ─────────────────────────────────────────
# #  1. ADD STUDENT
# # ─────────────────────────────────────────

# def add_student():
#     header("ADD STUDENT")

#     name   = input("  Student Name  : ").strip()
#     age    = input("  Age           : ").strip()
#     course = input("  Course        : ").strip()
#     email  = input("  Email         : ").strip()

#     if not all([name, age, course, email]):
#         print("\n  ❌  All fields are required.")
#         pause()
#         return

#     if not age.isdigit():
#         print("\n  ❌  Age must be a number.")
#         pause()
#         return

#     try:
#         with connect() as conn:
#             conn.execute(
#                 "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
#                 (name, int(age), course, email)
#             )
#         print("\n  ✅  Student added successfully!")
#     except sqlite3.IntegrityError:
#         print("\n  ❌  Email already exists.")

#     pause()


# # ─────────────────────────────────────────
# #  2. VIEW ALL STUDENTS
# # ─────────────────────────────────────────

# def view_students():
#     header("ALL STUDENTS")
#     with connect() as conn:
#         rows = conn.execute("SELECT * FROM students ORDER BY id").fetchall()
#     print_table(rows)
#     pause()


# # ─────────────────────────────────────────
# #  3. SEARCH STUDENT
# # ─────────────────────────────────────────

# def search_student():
#     header("SEARCH STUDENT")
#     print("  1. Search by ID")
#     print("  2. Search by Name")
#     choice = input("\n  Choose: ").strip()

#     with connect() as conn:
#         if choice == "1":
#             sid = input("  Enter Student ID: ").strip()
#             if not sid.isdigit():
#                 print("\n  ❌  ID must be a number.")
#                 pause()
#                 return
#             rows = conn.execute("SELECT * FROM students WHERE id = ?", (int(sid),)).fetchall()
#         elif choice == "2":
#             name = input("  Enter Name: ").strip()
#             rows = conn.execute(
#                 "SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",)
#             ).fetchall()
#         else:
#             print("\n  ❌  Invalid option.")
#             pause()
#             return

#     print_table(rows)
#     pause()


# # ─────────────────────────────────────────
# #  4. UPDATE STUDENT
# # ─────────────────────────────────────────

# def update_student():
#     header("UPDATE STUDENT")
#     sid = input("  Enter Student ID to update: ").strip()

#     if not sid.isdigit():
#         print("\n  ❌  ID must be a number.")
#         pause()
#         return

#     with connect() as conn:
#         row = conn.execute("SELECT * FROM students WHERE id = ?", (int(sid),)).fetchone()
#         if not row:
#             print("\n  ❌  Student not found.")
#             pause()
#             return

#         print(f"\n  Current → Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Email: {row[4]}")
#         print("  (Press Enter to keep current value)\n")

#         name   = input(f"  New Name   [{row[1]}]: ").strip() or row[1]
#         age    = input(f"  New Age    [{row[2]}]: ").strip() or str(row[2])
#         course = input(f"  New Course [{row[3]}]: ").strip() or row[3]
#         email  = input(f"  New Email  [{row[4]}]: ").strip() or row[4]

#         if not age.isdigit():
#             print("\n  ❌  Age must be a number.")
#             pause()
#             return

#         try:
#             conn.execute(
#                 "UPDATE students SET name=?, age=?, course=?, email=? WHERE id=?",
#                 (name, int(age), course, email, int(sid))
#             )
#             print("\n  ✅  Student updated successfully!")
#         except sqlite3.IntegrityError:
#             print("\n  ❌  Email already used by another student.")

#     pause()


# # ─────────────────────────────────────────
# #  5. DELETE STUDENT
# # ─────────────────────────────────────────

# def delete_student():
#     header("DELETE STUDENT")
#     sid = input("  Enter Student ID to delete: ").strip()

#     if not sid.isdigit():
#         print("\n  ❌  ID must be a number.")
#         pause()
#         return

#     with connect() as conn:
#         row = conn.execute("SELECT * FROM students WHERE id = ?", (int(sid),)).fetchone()
#         if not row:
#             print("\n  ❌  Student not found.")
#             pause()
#             return

#         print(f"\n  Found: {row[1]} — {row[3]} ({row[4]})")
#         confirm = input("  Are you sure you want to delete? (yes/no): ").strip().lower()

#         if confirm == "yes":
#             conn.execute("DELETE FROM students WHERE id = ?", (int(sid),))
#             print("\n  ✅  Student deleted.")
#         else:
#             print("\n  ℹ️   Deletion cancelled.")

#     pause()


# # ─────────────────────────────────────────
# #  6. EXPORT REPORT
# # ─────────────────────────────────────────

# def export_report():
#     header("EXPORT REPORT")
#     with connect() as conn:
#         rows = conn.execute("SELECT * FROM students ORDER BY id").fetchall()

#     if not rows:
#         print("\n  ❌  No students to export.")
#         pause()
#         return

#     filename = "student_report.txt"
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open(filename, "w") as f:
#         f.write("=" * 75 + "\n")
#         f.write("           STUDENT REGISTRATION REPORT\n")
#         f.write(f"           Generated: {timestamp}\n")
#         f.write("=" * 75 + "\n\n")
#         f.write(f"{'ID':<6} {'Name':<20} {'Age':<5} {'Course':<20} {'Email'}\n")
#         f.write("-" * 75 + "\n")
#         for r in rows:
#             f.write(f"{r[0]:<6} {r[1]:<20} {r[2]:<5} {r[3]:<20} {r[4]}\n")
#         f.write(f"\nTotal Students: {len(rows)}\n")

#     print(f"\n  ✅  Report saved to '{filename}'")
#     pause()


# # ─────────────────────────────────────────
# #  8. STATISTICS (BONUS)
# # ─────────────────────────────────────────

# def show_statistics():
#     header("STATISTICS")
#     with connect() as conn:
#         total  = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
#         avg    = conn.execute("SELECT AVG(age) FROM students").fetchone()[0]
#         oldest = conn.execute("SELECT name, age FROM students ORDER BY age DESC LIMIT 1").fetchone()
#         youngest = conn.execute("SELECT name, age FROM students ORDER BY age ASC LIMIT 1").fetchone()

#         courses = conn.execute(
#             "SELECT course, COUNT(*) as cnt FROM students GROUP BY course ORDER BY cnt DESC"
#         ).fetchall()

#     if total == 0:
#         print("\n  No data available.")
#         pause()
#         return

#     print(f"\n  Total Students     : {total}")
#     print(f"  Average Age        : {avg:.1f}")
#     print(f"  Oldest Student     : {oldest[0]} (Age {oldest[1]})")
#     print(f"  Youngest Student   : {youngest[0]} (Age {youngest[1]})")
#     print(f"\n  {'Course':<25} {'Students'}")
#     print("  " + "-" * 35)
#     for course, count in courses:
#         print(f"  {course:<25} {count}")

#     pause()


# # ─────────────────────────────────────────
# #  MAIN MENU
# # ─────────────────────────────────────────

# def main():
#     create_table()

#     while True:
#         clear()
#         header()
#         print("""
#   1. Add Student
#   2. View Students
#   3. Search Student
#   4. Update Student
#   5. Delete Student
#   6. Export Report
#   7. Exit
#   8. Calculate Statistics (Bonus)
#         """)
#         choice = input("  Choose an option: ").strip()

#         actions = {
#             "1": add_student,
#             "2": view_students,
#             "3": search_student,
#             "4": update_student,
#             "5": delete_student,
#             "6": export_report,
#             "8": show_statistics,
#         }

#         if choice == "7":
#             clear()
#             print("\n  👋  Goodbye!\n")
#             break
#         elif choice in actions:
#             clear()
#             actions[choice]()
#         else:
#             print("\n  ❌  Invalid option. Try again.")
#             pause()


# if __name__ == "__main__":
#     main()
