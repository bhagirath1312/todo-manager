from termcolor import colored  # type: ignore

class Todo_list:
    def __init__(self):
        self.list = []
        title = colored("Welcome To Todo List", "magenta", attrs=["bold"])
        print(title)
        self.menu()

    def menu(self):
        print("1. Display Todo List")
        print("2. Add Todo List")
        print("3. Save Todo File")
        print("4. Mark Todo List as Complete")
        print("5. Load Todo File")

        op = input("Choose Option 1 to 5:- ")

        if op == "1":
            self.display()
        elif op == "2":
            self.add()
        elif op == "3":
            self.save()
        elif op == "4":
            self.mark()
        elif op == "5":
            self.load()
        else:
            print(colored("Invalid option, please try again.", "red"))
            self.menu()

    def display(self):
        if not self.list:
            print(colored("Todo List is Empty!", "yellow"))
            self.add()
        else:
            print(colored("\nTodo List:", "cyan", attrs=["bold"]))
            for idx, todo in enumerate(self.list, start=1):
                status = (
                    colored("✓", "green") if todo["completed"] else colored("✗", "red")
                )
                print(f"{idx}. [{status}] {todo['task']}")

    def add(self):
        print(
            "Now you can Add Task\n If there are no next Task, enter (END) in the Task name.\n"
        )
        while True:
            i = input("Enter Task Name:- ")
            if i == "END":
                break
            self.list.append({"task": i, "completed": False})
        print(colored("Task Added", "green"))

        self.menu()

    def mark(self):
        self.display()
        if not self.list:
            return
        try:
            index = int(input("Enter the number of the todo to mark as complete: "))
            if 1 <= index <= len(self.list):
                self.list[index - 1]["completed"] = True
                print(
                    colored(
                        f'Todo "{self.list[index - 1]["task"]}" marked as complete!',
                        "green",
                    )
                )
                self.menu()
            else:
                print(colored("Invalid number.", "red"))
                self.menu()
        except ValueError:
            print(colored("Please enter a valid number.", "red"))

    def save(self):
        try:
            with open("list.txt", "w") as f:
                for todo in self.list:
                    f.write(f"{todo['task']},{todo['completed']}\n")
            print(colored("Todos saved successfully!", "green"))
            self.menu()
        except Exception as e:
            print(colored(f"Error saving todos: {e}", "red"))

    def load(self):
        try:
            with open("list.txt", "r") as file:
                self.list = []
                for line in file:
                    task, completed = line.strip().split(",", 1)
                    self.list.append({"task": task, "completed": completed == "True"})
            print(colored("Todos loaded successfully!", "green"))
            self.menu()
        except FileNotFoundError:
            print(colored("No saved todos found. Starting fresh.", "yellow"))

Todo_list()
