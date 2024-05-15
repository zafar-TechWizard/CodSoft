import json
import os
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

TODO_FILE = "./ToDo-app/todos.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def add_todo(todos):
    clear_screen()
    print(Fore.CYAN + "Add New Todo")
    print(Fore.CYAN + "============")

    title = input("Enter task title: ")
    description = input("Enter task description: ")

    todos.append({"title": title, "description": description, "completed": False})
    save_todos(todos)

    print(Fore.GREEN + "Todo added successfully!")

def view_todos(todos):
    clear_screen()
    print(Fore.CYAN + "Todo List")
    print(Fore.CYAN + "=========")

    if todos:
        for index, todo in enumerate(todos, start=1):
            status = Fore.GREEN + "Completed" if todo["completed"] else Fore.RED + "Pending"
            print(Fore.YELLOW + f"{index}. {todo['title']} - {status}")
    else:
        print(Fore.RED + "No todos found.")

def update_todo(todos):
    clear_screen()
    print(Fore.CYAN + "Update Todo")
    print(Fore.CYAN + "===========")

    view_todos(todos)
    choice = int(input(Fore.MAGENTA + "Enter the index of the todo to update: "))

    if 1 <= choice <= len(todos):
        todos[choice - 1]["completed"] = not todos[choice - 1]["completed"]
        save_todos(todos)
        print(Fore.GREEN + "Todo updated successfully!")
    else:
        print(Fore.RED + "Invalid index!")

def delete_todo(todos):
    clear_screen()
    print(Fore.CYAN + "Delete Todo")
    print(Fore.CYAN + "===========")

    view_todos(todos)
    choice = int(input(Fore.MAGENTA + "Enter the index of the todo to delete: "))

    if 1 <= choice <= len(todos):
        del todos[choice - 1]
        save_todos(todos)
        print(Fore.GREEN + "Todo deleted successfully!")
    else:
        print(Fore.RED + "Invalid index!")

def sort_todos(todos):
    todos.sort(key=lambda x: x["title"].lower())

def task_details(todos):
    clear_screen()
    print(Fore.CYAN + "Task Details")
    print(Fore.CYAN + "============")

    view_todos(todos)
    choice = int(input(Fore.MAGENTA + "Enter the index of the todo to view details: "))

    if 1 <= choice <= len(todos):
        print(Fore.YELLOW + "Title: " + todos[choice - 1]["title"])
        print(Fore.YELLOW + "Description: " + todos[choice - 1]["description"])
        print(Fore.YELLOW + "Status: " + (Fore.GREEN + "Completed" if todos[choice - 1]["completed"] else Fore.RED + "Pending"))
    else:
        print(Fore.RED + "Invalid index!")

def search_todos(todos):
    clear_screen()
    print(Fore.CYAN + "Search Todos")
    print(Fore.CYAN + "============")

    search_term = input("Enter search term: ").lower()

    results = [todo for todo in todos if search_term in todo["title"].lower() or search_term in todo["description"].lower()]
    if results:
        view_todos(results)
    else:
        print(Fore.RED + "No matching todos found.")

def main():
    todos = load_todos()

    while True:
        clear_screen()
        print("         " + Fore.CYAN + "To-Do List")
        print("    " + Fore.CYAN + "=======================")
        print("\n" + Fore.MAGENTA + "1. Add Todo")
        print(Fore.MAGENTA + "2. View Todos")
        print(Fore.MAGENTA + "3. Update Todo")
        print(Fore.MAGENTA + "4. Delete Todo")
        print(Fore.MAGENTA + "5. Sort Todos")
        print(Fore.MAGENTA + "6. Task Details")
        print(Fore.MAGENTA + "7. Search Todos")
        print(Fore.MAGENTA + "8. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
            input(Fore.YELLOW + "\nPress Enter to go back to the main menu...")
        elif choice == '3':
            update_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '5':
            sort_todos(todos)
            print(Fore.GREEN + "Todos sorted successfully!")
            time.sleep(1)
        elif choice == '6':
            task_details(todos)
            input(Fore.YELLOW + "\nPress Enter to go back to the main menu...")
        elif choice == '7':
            search_todos(todos)
            input(Fore.YELLOW + "\nPress Enter to go back to the main menu...")
        elif choice == '8':
            print(Fore.YELLOW + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice!")

        # Add a delay after each action for better user experience
        time.sleep(1)

if __name__ == "__main__":
    main()
