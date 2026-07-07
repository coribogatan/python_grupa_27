import json
from asyncio import tasks
from pathlib import Path

file_categ = "file_categories.json"
to_do_list = "file_tasks.json"

def write_data(file_name, data):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    # write data to file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_data(file_name):
    path = Path(file_name)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def add_categories():
    categories = read_data(file_categ)

    print("Enter Categories (write stop to stop):")

    while True:
        category = input("Category: ")

        if category.lower() == "stop":
            break

        if category not in categories:
            categories.append(category)
        else:
             print("Category already exist")

    write_data(file_categ, categories)
    return categories

def show_categories(categories):
    print("\nExisting Categories:\n")
    for category in categories:
        print(category)


class Task:
    def __init__(self, title, date, owner, category):
        self.title = title
        self.date = date
        self.owner = owner
        self.category = category
        self.completed = False

    def __str__(self):
        return f"{self.title}, {self.date}, {self.owner}, {self.category}, completed = {self.completed}"

    def __repr__(self):
        return f'Task("{self.title}", "{self.date}", "{self.owner}", {self.category})'

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "owner": self.owner,
            "category": self.category,
            "completed": self.completed
        }


def add_task(categories):
    tasks = read_data(to_do_list)

    while True:
        title = input("New Task: ")
        date = input("Data limita (ex: ex:  22.01.2022 21:30): ")
        owner = input("Persoana responsabilă: ")
        category = input("Categoria: ")

        if category not in categories:
            print("Error! Category does not exist and the task is not saved in the to-do list")
        elif any(
            task["title"] == title and
            task["date"] == date and
            task["owner"] == owner and
            task["category"] == category
            for task in tasks
        ):
            print("This task already exists.")
        else:
            task_new = Task(
                title,
                date,
                owner,
                category
            )

            tasks.append(task_new.to_dict())
            write_data(to_do_list, tasks)

            print("Task adăugat cu succes!")

        raspuns = input("Mai adăugați un task? (yes/no): ").lower()
        if raspuns != "yes":
            break


def todolist():
    categories = read_data(file_categ)

    if len(categories) == 0:
        categories = add_categories()

    while True:
        print("\n======= To Do List =======")
        print("1. Adaugă categorii")
        print("2. Afișează categorii")
        print("3. Adaugă task")
        print("4. Afișează task-urile")
        print("5. Ieșire")

        option = input("Alege opțiunea: ")

        if option == "1":
            categories = add_categories()

        elif option == "2":
            show_categories(categories)

        elif option == "3":
            add_task(categories)

        elif option == "4":
            file_data = read_data(to_do_list)
            print(file_data)

        elif option == "5":
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă!")


todolist()