class ToDoList:
    def _init_(self):  # Fixing the constructor method
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def update_task(self, index, updated_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = updated_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the index of the task to update: ")) - 1
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(index, updated_task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":  # Fixing the module name check
    main()