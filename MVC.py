class Model:
    def __init__(self):
        # Initialize an empty list to hold tasks.
        self.tasks = []
    # Adds a task to the list of tasks.
    def add_task(self, task):
        self.tasks.append(task)
    # Returns the list of tasks.
    def get_tasks(self):
        return self.tasks

# View class responsible for
# handling user interaction and display.
class View:
    # Reads a task from the user.
    def input_task(self):
        return input("Input task:\n")

    # Displays the list of tasks to the user.
    def show_tasks(self, tasks):
        for item in tasks:
            print(item)

    # Shows the menu and returns the user's choice.
    def show_menu(self):
        print("*************************")
        print("1 - Add task")
        print("2 - Show tasks")
        print("3 - Exit")
        result = int(input("Choose what to do:\n"))
        print("*************************")
        return result

    # Controller class to act
    # as an intermediary between the Model and View.
class Controller:
    # Initialize the Controller with a Model and a View.
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Method to handle adding a new task.
    def action_input_task(self):
        task = self.view.input_task()
        self.model.add_task(task)

    # Method to handle showing the list of tasks.
    def action_show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

# Initialize the MVC components.
obj_controller = Controller(Model(), View())

# Main application loop.
while True:
    # Display menu and get user choice.
    result = obj_controller.view.show_menu()

    # Match user choice to appropriate action.
    match result:
        case 1:
            # Add a new task.
            obj_controller.action_input_task()
        case 2:
            # Show list of tasks.
            obj_controller.action_show_tasks()
        case 3:
            # Exit the application.
            print("Bye!")
            break
        case _:
            # Handle invalid user input.
            print("\nWrong choice. Try again!\n")