
def add():
    item = input("Write a todo: ")
    return item

def remove():
    index = input("Enter a todo index to remove: ")
    return index

def display():
    print(List)

is_running = True
List = []

while is_running == True:
    print("To-Do List")
    print("1. See list")
    print("2. Add todo")
    print("3. Remove todo")
    print("4. Exit")

    choice = input("Enter a choice:")

    if choice == "1":
        display()

    elif choice == "2":
        add()
    
    elif choice == "3":
        remove()
    
    elif choice == "4":
        is_running = False

    else:
        print("Not valid")


