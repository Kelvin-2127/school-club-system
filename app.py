from models import create_tables
from db import get_connection

def add_club():
    name = input("Club name: ")
    description = input("Description: ")
    club_id = input("Club id: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO clubs (name, description, club_id) VALUES (%s, %s, %s)",
        (name, description, club_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Club added!")

def view_clubs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM clubs")
    clubs = cur.fetchall()
    if clubs:
        for club in clubs:
            print(f"ID: {club[0]}, Name: {club[1]}, Description: {club[2]}")
    else:
        print("No clubs found.")
    cur.close()
    conn.close()

def delete_club():
    club_id = input("Enter Club ID to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM clubs WHERE id=%s RETURNING id", (club_id,))
    if cur.fetchone():
        conn.commit()
        print("✅ Club deleted!")
    else:
        print("❌ Club ID not found.")
    cur.close()
    conn.close()

def add_student():
    name = input("Student name: ")
    email = input("Email: ")
    student_id = input("Student id: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, email, student_id) VALUES (%s, %s, %s)",
        (name, email, student_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Student added!")

def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM students")
    students = cur.fetchall()
    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")
    else:
        print("No students found.")
    cur.close()
    conn.close()

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s RETURNING id", (student_id,))
    if cur.fetchone():
        conn.commit()
        print("✅ Student deleted!")
    else:
        print("❌ Student ID not found.")
    cur.close()
    conn.close()

def join_club():
    student_id = input("Student ID: ")
    club_id = input("Club ID: ")

    conn = get_connection()
    cur = conn.cursor()
    # Validate student
    cur.execute("SELECT id FROM students WHERE id=%s", (student_id,))
    if not cur.fetchone():
        print("❌ Student not found.")
        cur.close()
        conn.close()
        return
    # Validate club
    cur.execute("SELECT id FROM clubs WHERE id=%s", (club_id,))
    if not cur.fetchone():
        print("❌ Club not found.")
        cur.close()
        conn.close()
        return
    # Check if already a member
    cur.execute("SELECT id FROM memberships WHERE student_id=%s AND club_id=%s", (student_id, club_id))
    if cur.fetchone():
        print("❌ Student already in club.")
        cur.close()
        conn.close()
        return
    # Add membership
    cur.execute("INSERT INTO memberships (student_id, club_id) VALUES (%s, %s)", (student_id, club_id))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Student joined club!")

def exit_club():
    student_id = input("Student ID: ")
    club_id = input("Club ID: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM memberships WHERE student_id=%s AND club_id=%s RETURNING id", (student_id, club_id))
    if cur.fetchone():
        conn.commit()
        print("✅ Student exited club!")
    else:
        print("❌ Membership not found.")
    cur.close()
    conn.close()

def menu():
    create_tables()
    while True:
        print("\n--- School Club System ---")
        print("1. Add Club")
        print("2. View Clubs")
        print("3. Delete Club")
        print("4. Add Student")
        print("5. View Students")
        print("6. Delete Student")
        print("7. Join Club")
        print("8. Exit Club")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "1": add_club()
        elif choice == "2": view_clubs()
        elif choice == "3": delete_club()
        elif choice == "4": add_student()
        elif choice == "5": view_students()
        elif choice == "6": delete_student()
        elif choice == "7": join_club()
        elif choice == "8": exit_club()
        elif choice == "9": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    menu()