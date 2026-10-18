tasks = []
def print_menu():
    print("=" * 5, "Task Manager", "=" * 5)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
while True:
    print_menu()
    try:
        choice = int(input("Enter option of your choice : "))
    except ValueError:
        print("Please enter valid number.")
        continue
    if choice == 1:
        task = (input("Enter your task : "))
        tasks.append({"name": task, "completed": False})
        print("Task added successfully")
        print()
    elif choice == 2:
         if not tasks:
            print("No tasks available")
         else:
           for task in tasks:
               if task["completed"] == True:
                   print(f"{task['name']} - Completed")
               else:
                   print(f"{task['name']} - Pending")
    elif choice == 3:
        task_name = input("Enter the task to complete : ")
        found = False
        for task in tasks:
            if task_name == task["name"]:
                task["completed"] = True
                found = True
                print(f"The {task['name']} task is marked as completed successfully")
                break
        if not found:
            print("Task not found")
    elif choice == 4:
        delete = input("Enter the task you want to delete : ")
        found = False
        for task in tasks:
            if delete == task['name']:
                tasks.remove(task)
                found = True
                print("Task deleted successfully")
                break
        if not found:
            print("Task not found")
    elif choice == 5:
        print("Exiting Task manager")
        break
    else:
        print("Invalid choice, Please try again")