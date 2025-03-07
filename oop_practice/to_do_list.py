# to_do_list.py

# To-Do List Manager
# * Define a Task class with attributes
#   description, due_date, and completed.
# * Implement methods to mark_complete(),
#   edit_task(), and show_task_details().
# * Store multiple tasks in a ToDoList class and
#   allow searching and sorting.

from time import sleep

class Task:
    def __init__(self, description: str, due_date: str, completed: bool):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True
    
    def edit_task(self):
        desc_flag = input('Do you want to change the task description? Type y or n: ')
        if desc_flag == 'y':
            self.description = input('Enter the new task description: ')
        date_flag = input('Do you want to change the task due date? Type y or n: ')
        if date_flag == 'y':
            self.due_date = input('Enter the new due date: ')

    def show_task_details(self):
        print(f'Task Description: {self.description}')
        print(f'Task Due Date: {self.due_date}')
        print(f'Completed: {self.completed}')
    
class ToDoList:
    pass

taxes = Task('Prepare Federal and State income tax returns.', 'April 15, 2025', False)
taxes.show_task_details()
taxes.edit_task()
taxes.show_task_details()
print('The processor is finishing your taxes. ')
sleep(5)
taxes.mark_complete()
taxes.show_task_details()