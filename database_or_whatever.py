import time
import sys
import csv


objects = []
unsaved_objects = []

def main():

    with open("database.csv","r") as file:
        reader = csv.DictReader(file)
        for stuff in reader:
            print("Name: " + stuff["name"],"Age: " + stuff["age"])
        
    time.sleep(2)

    while True:
        print("===== DATABASE =====")
        print("1. Add Object")
        print("2. Search Object")
        print("3. Remove Object")
        print("4. Search Objects")
        print("5. Save Object")
        print("6. Exit")

        choice = input("").lower().strip()

        try:
            if choice == "1" or choice == "add object":
                add_object()
            elif choice == "2" or choice == "search object":
                search_object()
            elif choice == "3" or choice == "remove object":
                remove_object()
            elif choice == "4" or choice == "search objects":
                search_objects()
            elif choice == "5" or choice == "save object":
                save_object()
            elif choice == "6" or choice == "exit":
                exit()
            else:
                print("Wrong input. Expecting number or name in the list.")

        except ValueError:
            print("uh... nope")


def add_object():

    name = input("Name: ")
    age = input("Age: ")

    new_entry = {"name": name, "age": age}
    objects.append(new_entry)
    unsaved_objects.append(new_entry)

    print(f"Added {name}.")
    time.sleep(0.5)
    

def search_object():
    found = False

    object_search = input("CASE SENSITIVE! ")
    for obj in objects: 
        if obj["name"] == object_search:
            print("name: "+ obj["name"], "age: " + obj["age"])
            found = True

    if not found:
        print("No such thing as "+ object_search)
    
    time.sleep(0.5)    

def remove_object():

    remover = input("Who do you want to remove? CASE SENSITIVE ")
    found = False
    for obj in list(objects):
        if obj["name"] == remover:
            objects.remove(obj)
            if obj in unsaved_objects:
                unsaved_objects.remove(obj)
            found = True

    if not found:
        print("such user does not exist.")
    
    time.sleep(0.5)
    

def search_objects():
    for objecter in objects:
        print("name: " + objecter["name"], "age: " + objecter["age"])
        
    time.sleep(0.5)
    

def save_object():

    if not objects:
        print("no objects")
        return

    writing_objects = objects

    with open("database.csv", "a", newline="") as file:
        fieldnames = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

      
        writer.writerows(unsaved_objects)

    print(f"Successfully saved {len(unsaved_objects)} object(s) to CSV.")

   
    unsaved_objects.clear()

       


        
    
    time.sleep(0.5)
    

def exit():
    sys.exit("Exited")









if __name__ == "__main__":
    main()