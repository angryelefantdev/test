import time
import sys

objects = []

def main():

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

    objects.append({"name": name,"age": age})

    
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
    for removed in objects:
        if removed["name"] == remover:
            objects.remove(removed)
            found = True

    if not found:
        print("such user does not exist.")
    
    time.sleep(0.5)
    

def search_objects():
    print("searched for objects")
    time.sleep(0.5)
    

def save_object():
    print("saved objects")
    time.sleep(0.5)
    

def exit():
    sys.exit("Exited")









if __name__ == "__main__":
    main()