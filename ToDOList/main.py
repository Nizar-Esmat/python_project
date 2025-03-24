# to do list
tasks = []
def main():
        massage ="""
        1. add a new task
        2. mark a task as done      
        3. view all tasks
        4. exit 
        """
        
        while True:
            print(massage)
            choice = input("Enter your choice: ")   
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
              mark_task_as_done(tasks)
            elif choice == "3":
                view_tasks(tasks)       
            elif choice == "4":
                break
            else:
                print("Invalid choice enter any number from 1 to 4")
                
                
        print("Thank you for using the program")
        print("Goodbye!")
    
def add_task(task_list):
    task = input("Enter a new task: ")

    new_task = {"task": task, "done": False}
    task_list.append(new_task)
    print("Task added successfully")
    
def mark_task_as_done(task_list):
    tasksNotDone = [task for task in task_list if not task["done"]]
    
    for index , value in enumerate(tasksNotDone):
        print(f"{index + 1}. {value['task']} - Not done")
        
    print("-" *20)
    if not tasksNotDone:
        print("No tasks to mark as done")
    else:
        try:
            task_number = int(input("Enter the task number to mark as done: "))
            tasksNotDone[task_number - 1]["done"] = True
            print("Task marked as done")
        except ValueError:
            print("Invalid input")

def view_tasks(task_list):
    if not task_list:
        print("No tasks to view")
    else : 
        print("All tasks")
        for index , value in enumerate(task_list):
            status = "Done" if value["done"] else "Not done"
            print("-" * 20)
            print(f"{index + 1}. {value['task']} - {status}")
        
    
if __name__ == "__main__":
    main()