tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def show_tasks():
    print("Your tasks:")
    for t in tasks:
        print("-", t)

add_task("Learn Git")
show_tasks()