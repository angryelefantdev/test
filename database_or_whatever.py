import csv
import sys
import time

objects = []


def main():
    try:
        with open("database.csv", "r") as file:
            reader = csv.DictReader(file)
            for stuff in reader:
                print("Name: " + stuff["name"], "Age: " + stuff["age"])
                objects.append({"name": stuff["name"], "age": stuff["age"]})
    except FileNotFoundError:
        print("No existing database file found. A new one will be created on save.")

    time.sleep(1)

    while True:
        print("\n===== DATABASE =====")
        print("1. Add Object")
        print("2. Search Object")
        print("3. Remove Object")
        print("4. Search Objects")
        print("5. Save Changes")
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
            elif choice in ("5", "save object", "save changes"):
                save_object()
            elif choice in ("6", "exit"):
                exit_app()
            else:
                print("Wrong input. Expecting number or name in the list.")

        except ValueError:
            print("Invalid input.")


def add_object():
    name = input("Name: ")
    age = int(input("Age: "))
    


    new_entry = {"name": name, "age": age}
    objects.append(new_entry)

    print(f"Added {name}.")
    time.sleep(0.5)


def search_object():
    found = False
    object_search = input("CASE SENSITIVE! ")
    for obj in objects:
        if obj["name"] == object_search:
            print("name: " + obj["name"], "age: " + obj["age"])
            found = True

    if not found:
        print("No such thing as " + object_search)

    time.sleep(0.5)


def remove_object():
    remover = input("Who do you want to remove? CASE SENSITIVE ")
    found = False

    for obj in list(objects):
        if obj["name"] == remover:
            objects.remove(obj)
            found = True

    if found:
        print(f"Removed {remover} from memory. Remember to select 'Save' to update database.csv!")
    else:
        print("Such user does not exist.")

    time.sleep(0.5)


def search_objects():
    if not objects:
        print("Database is empty.")
        return

    for objecter in objects:
        print("name: " + objecter["name"], "age: " + objecter["age"])

    time.sleep(0.5)


def save_object():
    # Write mode ("w") overwrites the file with the updated 'objects' list
    with open("database.csv", "w", newline="") as file:
        fieldnames = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(objects)

    print(f"Successfully saved {len(objects)} object(s) to database.csv.")
    time.sleep(0.5)


def exit_app():
    sys.exit("Exited")


if __name__ == "__main__":
    main()