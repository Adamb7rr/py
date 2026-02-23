    user = int(input("Enter task number to delete: "))
            if 0 <= user - 1 < len(lines):
                with open('tasks.txt', 'r') as file:
                    lines = file.readlines()
                del lines[user - 1]
                with open("tasks.txt", 'w')as file:
                    file.writelines(lines)