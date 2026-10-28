import json

def add_task():
    task = {
        "task": input("Add your task: "),
        "status": "not completed"
    }
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        tasks.append(task)
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
    return

def show_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        for i, v in enumerate(tasks, start = 1):
            print(f"{i}. {v['task']}. {v['status']}")
    return

def complete_task():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        task_name = input("What task do you want to complete?: ")
        for task in tasks:
            if task['task'] == task_name:
                task['status'] = "completed"
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file)
                print("Task Completed!")
                break
        else:
            print("Task not found!")
    return

def delete_task():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        task_name = input("What task do you want to delete?: ")
        for task in tasks:
            if task["task"] == task_name:
                tasks.remove(task)
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file)
                    print("Task Deleted!")
                    break
        else:
            print("Task not found!")
    return


#MAIN_MENU
print("====== TASK MANAGER ======\n1.Add Task\n2.show Tasks\n3.Complete Task\n4.Delete Task\n5.Exit")
while True:
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please choose from 1 to 5!")
        continue
    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        break