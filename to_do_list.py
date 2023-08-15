tasks = []

# def read_tasks_from_file(filename):
#     with open (filename , "r")as file:
#         lines = file.readlines()
#         tasks = [line.strip() for line in lines]
#     return tasks
# tasks=read_tasks_from_file("tasks.txt")

def write_to_file(data):
    print(data)
    with open('tasks.txt', 'w') as file:
        for task in data:
            file.write(str(task))
            file.write(str("\n"))


def add_task(task , status):
    tasks.append({"task":task , "status":status})
    print("you have added a task", task , "with status:" , status)
    

def show_tasks():
    print("To do list")
    for index,task_info in enumerate(tasks , start=1):
        task = task_info["task"]
        status = task_info["status"]
        print(f"{index}. Task: {task} - Status:{status}")

def delete_task(index):
    if 1<=index <= len(tasks):
        deleted_task = tasks . pop(index - 1)
        print("the delete had done", deleted_task)
    else:
        print("the num you enter did not excect")

while True:
        print("choose a Procedure:")
        print("1.Add task")
        print("2.Show tasks")
        print("3.Delete task")
        print("4.Exit")

        choice = input("Enter the Procedure num from(1,2,3,4)")

        if choice=="1":
             new_task = input("Enter new task")
             status = input("Enter the task status(Done,In progress,Later)")
             add_task(new_task , status)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            index_to_delete =int(input("Enter the task number to be deleted:"))
            delete_task(index_to_delete)

        elif choice == "4":
            print("Exit done")
            write_to_file(tasks)
            break

        else:
            print("wrong choice")
        
            
            



