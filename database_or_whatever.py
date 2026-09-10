import sys
import time
import sqlite3

connection = sqlite3.connect("thedatabase.db")
cursor = connection.cursor()

def main():
    command_create = """
    CREATE TABLE IF NOT EXISTS the_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )"""
    cursor.execute(command_create)
    connection.commit()

    cursor.execute("SELECT * FROM the_data")
    rows = cursor.fetchall()

    if not rows:
        print("Nothing in the database yet.")
    else:
        for row in rows:
            print(row)

    time.sleep(1)

    while True:
        print("\n===== DATABASE =====")
        print("1. Add Object")
        print("2. Search Object")
        print("3. Remove Object")
        print("4. Search Objects")
        print("5. Save Object")
        print("6. Exit")

        choice = input("Choice: ").lower().strip()

        try:
            if choice in ("1", "add object"):
                add_object()
            elif choice in ("2", "search object"):
                search_object()
            elif choice in ("3", "remove object"):
                remove_object()
            elif choice in ("4", "search objects"):
                search_objects()
            elif choice in ("5", "save object"):
                save_object()
            elif choice in ("6", "exit"):
                exit_app()
            else:
                print("Wrong input. Expecting number or name in the list.")
        except ValueError:
            print("Invalid input.")


def add_object():
    name = input("Name: ")
    try:
        age = int(input("Age: "))
        cursor.execute("INSERT INTO the_data (name, age) VALUES (?, ?)", (name, age))
        connection.commit() 
        print(f"Added {name}.")
    except ValueError:
        print("Age must be a valid number.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    time.sleep(0.5)


def search_object():
    find_object = input("Who do you wish to find? ")
    try:
        cursor.execute("SELECT name, age FROM the_data WHERE name = ?", (find_object,))
        results = cursor.fetchall()

        if not results:
            print(f"Couldn't find '{find_object}'.")
        else:
            for row in results:
                print(f"Name: {row[0]}, Age: {row[1]}")

    except sqlite3.Error as error:
        print(f"Error: {error}")
    time.sleep(0.5)


def remove_object():
    object_remover = input("Who do you wish to remove? ")
    cursor.execute("DELETE FROM the_data WHERE name = ?", (object_remover,))
    connection.commit()  # Save deletion
    print(f"Removed '{object_remover}'")
    time.sleep(0.5)


def search_objects():
    cursor.execute("SELECT * FROM the_data")
    rows = cursor.fetchall()
    
    if not rows:
        print("Database is currently empty.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]}")

    time.sleep(0.5)


def save_object():
    connection.commit()
    print("Database changes saved successfully!")
    time.sleep(0.5)


def exit_app():
    connection.close() 
    sys.exit("Exited")


if __name__ == "__main__":
    main()