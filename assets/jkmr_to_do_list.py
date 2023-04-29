#
# CSC.130.0001 Group Project
# Roberto Cipriano, Morgan Mach, Kelly Hamilton, Jordan Manus
#
# This program is a fully functional To-Do List, with the ability to
# add tasks, save tasks, modify tasks, display tasks,and mark them as complete.
# There is also a manual save and load feature, as well as an autosave feature
# in the event that the user enters '9' to exit.
#

import time


def modification_validation(task):
    if task == "" or task.isdigit():
        task = input("Invalid Entry. Enter a task: ").upper()

    elif task not in todo_list.tasks or todo_list.completed_tasks:
        task = input("Task not in list. Try again: ").upper()
    return task


def priority_validation(priority):
    while priority == "":
        # raise ValueError("Priority cannot be blank")
        priority = input("Invalid entry. Enter a priority rating (1-5): ")
    while int(priority) <= 0 or int(priority) > 5:
        priority = input("Invalid entry. Enter a priority rating (1-5): ")
    return priority


class TodoList:
    def __init__(self):
        self.tasks = {}  # initialize an empty dictionary to store the tasks.
        self.completed_tasks = []  # initialize empty list to store tasks

    # Validate input task, then return it
    def entry_validation(self, task):
        while task == "" or task.isdigit():
            task = input("Invalid Entry. Enter a task: ").upper()

        while task in self.tasks:
            task = input("Task already in list. Enter a new task: ").upper()
        return task

    # Validate input task for modification and return it

    # Validate input priority and return it

    # Add a task to the todolist dictionary with its priority.
    def add_task(self, task, priority):
        if task in self.tasks:
            print("Task already exists.")
        else:
            self.tasks.update({task: priority})
            print(f'\nTask "{task}" has been added with a priority of: {priority}.')

    # Remove a task from either incomplete tasks list or complete tasks dictionary
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.pop(task)
            print(f'Task "{task}" successfully removed.')
        elif task in self.completed_tasks:
            self.completed_tasks.remove(task)
            print(f'Completed task "{task}" successfully removed.')
        else:
            print(f"Task '{task}' not found.")

    # Modify existing task by removing old task from list, and adding new task.
    def modify_task(self, old_task, new_task, new_priority=None):
        # get the original priority of the old task
        old_priority = None
        for task in self.tasks:
            if task[1] == old_task:
                old_priority = task[0]
            break
        if new_priority:
            self.remove_task(old_task)
            self.add_task(new_task, new_priority)
        else:
            self.remove_task(old_task)
            self.add_task(new_task, old_priority)

    # Mark a task as complete by appending the task to the completed tasks
    # Then deleting it from tasks list.
    def mark_complete(self, task):
        if task in self.tasks:
            self.completed_tasks.append(task)
            del self.tasks[task]
            print(f'\nTask "{task}" marked as complete.')
        else:
            print(f"Task '{task}' not found.")

    # Display current task list
    # Takes optional argument of status, and depending on input
    # Returns List/Complete, List, or Completed
    def display_todo(self, status='1'):

        sorted_priority = sorted(self.tasks.items(), key=lambda x: x[1])

        if status == '1':
            print("\nAll Tasks:")
            print("--------------------------------------------------------------")
            for task, priority in sorted_priority:
                print(f"- {task:<30}:\t\t Priority {priority:>8}")
                # print(sorted_priority)
            for task in self.completed_tasks:
                print(f"[COMPLETE] {task:>20}")
            input('Press "ENTER" to continue. . .')

        elif status == '2':
            print("\nIncomplete Tasks:")
            print("--------------------------------------------------------------")
            for task, priority in self.tasks.items():
                if task not in self.completed_tasks:
                    print(f"- {task:<30}: Priority {priority:>8}")
            input('Press "ENTER" to continue. . .')

        elif status == '3':
            print("\nCompleted Tasks:")
            print("--------------------------------------------------------------")
            if len(self.completed_tasks) == 0:
                print('No completed tasks to display.')
            else:
                for task in self.completed_tasks:
                    print("- [COMPLETE] " + task)
            input('Press "ENTER" to continue. . .')

        else:
            return "Invalid entry. Please enter '1' to display all tasks, enter '2' for incomplete tasks, or enter '3' for complete tasks."

    # removes all tasks from the task list,
    # As well as all tasks from the completed_tasks list
    # essentially initializes as new dictionary and list.
    def clear_all_tasks(self):
        self.tasks = {}
        self.completed_tasks = []

    # Takes file name input and writes current
    # Task dictionary and Completed Tasks list to file named after filename input
    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.tasks))

    # Takes filename input, searches for it and opens the file
    # Loading Completed Tasks list and Lists dictionary.
    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.tasks = eval(f.read())
        except FileNotFoundError:
            print(f"No file named {filename} found. Returning to main function.")
            return


todo_list = TodoList()  # create an instance of the TodoList class


class main:
    print("Welcome to JKMR To-Do List. Choose one of the following selections: ")

    # Main Menu Loop, prompting user for input choice regarding
    while True:
        choice = input(
            "\n1 - Add Task with its priority rating\n2 - Delete Task\n3 - Modify Task\n4 - Mark Task as Complete\n5 "
            "- Show Task List\n6 - Save Task List \n7 - Load Task List \n8 - Clear All Tasks \n9 - Exit Program\n\nEnter your choice: ")

        if choice == "1":
            task = input("Enter a task: ").upper()
            task = todo_list.entry_validation(task)
            priority = input("Enter a priority rating (1-5): ")
            priority = priority_validation(priority)
            todo_list.add_task(task, priority)

        elif choice == "2":
            task = input("Enter the task to remove: ").upper()
            todo_list.remove_task(task)

        elif choice == "3":
            old_task = input("Enter the task to modify: ").upper()
            old_task = modification_validation(old_task)
            new_task = input("Enter the new task name: ").upper()
            new_task = todo_list.entry_validation(new_task)
            new_priority = input("Enter the new priority rating: ")
            new_priority = priority_validation(new_priority)
            if new_priority:
                todo_list.modify_task(old_task, new_task, new_priority)
            else:
                todo_list.modify_task(old_task, new_task)

        elif choice == "4":
            task = input("Enter the task to mark as complete: ").upper()
            task = modification_validation(task)
            todo_list.mark_complete(task)

        elif choice == "5":
            status = input(
                "Enter '1' for all tasks, '2' for incomplete tasks, or '3' for completed tasks: ")
            while status not in "1, 2, 3" or status == "":
                status = input(
                    "Invalid entry. Enter '1' for all tasks, '2' for incomplete tasks, or '3' for completed tasks: ")
            todo_list.display_todo(status)

        elif choice == "6":
            filename = input("Enter a filename to save your tasks to (enter CANCEL to return to selection menu): ")
            if filename.lower() == 'cancel':
                print('\nSave file canceled. Returning to selection menu: \n')
                continue
            else:
                print(f'\nSaving file as: "{filename}." Please do not turn off your system.')
                todo_list.save_tasks_to_file(filename)
                print(f'File "{filename}" saved successfully.')

        elif choice == "7":
            filename = input("Enter the filename to load tasks from (enter CANCEL to return to selection menu: ")
            if filename.lower() == 'cancel':
                print('\nLoad file canceled. Returning to selection menu: \n')
                continue
            else:
                print(f'\nLoading "{filename}" file. . .')
                todo_list.load_tasks_from_file(filename)
                print(f'File "{filename}" successfully loaded.')

        elif choice == "8":
            print("Clearing all tasks.")
            time.sleep(1)
            print("Please wait . . .")
            time.sleep(2)
            print("All Tasks Cleared")
            time.sleep(1)
            todo_list.clear_all_tasks()

        elif choice == "9":
            print("Saving to autosave.txt")
            time.sleep(1)
            print("Please wait. . . .")
            time.sleep(2)
            print("Saved!")
            time.sleep(2)
            print("Goodbye!")
            time.sleep(1)
            filename = "autosave"
            todo_list.save_tasks_to_file(filename)
            break
        else:
            print("Invalid choice Please enter a valid choice.")
