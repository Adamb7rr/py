import os

def add_task():
    user_add = input("Enter discription of task: ")
    with open("tasks.txt", 'a') as file:
        file.write(f'{user_add}\n')
    print("Added!")

def view_tasks():
    n = 1
    with open('tasks.txt', 'r') as file:
        if os.path.getsize("tasks.txt") == 0:
            print("No tasks found.")
        lines = file.readlines()
        for line in lines:
            print(f"{n}. {line}")
            n += 1

def delete_task():
    try:
        user = int(input("Enter task number to delete: "))
        with open('tasks.txt', 'r') as file:
                lines = file.readlines()
        if 0 <= user - 1 < len(lines):
            del lines[user - 1]
            with open("tasks.txt", 'w')as file:
                file.writelines(lines)
                print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError as e:
        print(e)

def main():
    while True:
        try:
            print("_"*20)
            print("1. Add Task\n" \
            "2. View Tasks\n" \
            "3. Delete Task\n" \
            "4. Exit")
            user = input("> ")
            print("\n")
            if user == '1':
                add_task()
            elif user == '2':
                view_tasks()
            elif user == '3':
                delete_task()
            elif user == '4':
                print("Goodbye!")
                break
            else:
                raise ValueError("Only '1', '2', '3', '4'.")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()