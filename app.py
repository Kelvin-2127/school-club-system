from models import create_tables
from db import get_connection

def add_club():
    name = input("Club name: ")
    description = input("Description: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clubs (name, description) VALUES (%s, %s)",
        (name, description)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Club added!")


def view_clubs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM clubs")
    clubs = cur.fetchall()

    for club in clubs:
        print(club)

    cur.close()
    conn.close()


def add_student():
    name = input("Student name: ")
    email = input("Email: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Student added!")


def join_club():
    student_id = input("Student ID: ")
    club_id = input("Club ID: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO memberships (student_id, club_id) VALUES (%s, %s)",
        (student_id, club_id)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Student joined club!")


def menu():
    create_tables()

    while True:
        print("\n--- School Club System ---")
        print("1. Add Club")
        print("2. View Clubs")
        print("3. Add Student")
        print("4. Join Club")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_club()
        elif choice == "2":
            view_clubs()
        elif choice == "3":
            add_student()
        elif choice == "4":
            join_club()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()