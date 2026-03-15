import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
department TEXT,
email TEXT
)
""")

def add_student():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    email = input("Enter email: ")

    cursor.execute("INSERT INTO students(name, department, email) VALUES(?,?,?)",(name,dept,email))
    conn.commit()
    print("Student added successfully")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    
    if len(data) == 0:
        print("No students found")
    else:
        for row in data:
            print(row)

def delete_student():
    sid = input("Enter Student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student deleted successfully")
    else:
        print("Student ID not found")

while True:
    print("\n1 Add Student")
    print("2 View Students")
    print("3 Delete Student")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")