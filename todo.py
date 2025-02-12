#!/usr/bin/python3
"""Python program to manage a todolist"""

import sys
import datetime


class TodoElement:
    """Todo Element"""

    def __init__(self):
        self.category: str = ""
        self.name: str = ""
        self.duedate: datetime.date = datetime.datetime.today().date()
        self.priority: int = 0

    def from_storage(self, string: str) -> None:
        string_elements: list[str] = string.split(";")
        if len(string_elements) != 4:
            raise ValueError("Invalid string length: " + string)

        self.category = string_elements[0]
        self.name = string_elements[1]

        year, month, day = (int(element) for element in string_elements[2].split("-"))
        self.duedate = datetime.date(year, month, day)

        self.priority = int(string_elements[3])

    def to_storage(self) -> str:
        return f"{self.category};{self.name};{self.duedate};{self.priority}"

    def from_input(
        self, category: str, name: str, duedate: str = "", priority: str = "0"
    ) -> None:
        self.category = category
        self.name = name

        if duedate == "":
            self.duedate = datetime.datetime.today().date()
        else:
            try:
                year, month, day = (int(element) for element in duedate.split("-"))
                self.duedate = datetime.date(year, month, day)
            except ValueError:
                raise ValueError("Invalid date: " + duedate)

        if priority == "":
            self.priority = 0
        else:
            try:
                self.priority = int(priority)
            except ValueError:
                raise ValueError("Invalid priority: " + priority)

    def __str__(self) -> str:
        return f"{self.duedate}: {self.category} {self.name}, P{self.priority}"


def read_from_file(filename: str) -> list[TodoElement]:
    result: list[TodoElement] = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            element = TodoElement()
            element.from_storage(line.strip())
            result.append(element)

    return result


def write_to_file(filename: str, todolist: list[TodoElement]) -> None:
    result = ""
    for element in todolist:
        result += f"{element.to_storage()}\n"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(result)


def main() -> None:
    filename = "todolist/todo.txt"  # Please change this when you use the script
    args = sys.argv[1:]

    if len(args) == 0:
        print(
            """
------------------------------------------------
Adding a new task

    ./todo.py add <category> <name> <due date> <priority>

    due date and priority are optional. If due date is not given, the current date is used. If priority is not given, priority 0 is used.

    If you want to specify a priority without specifying a due date, you need to enter "" as due date.

    The format for the due date is yyyy-mm-dd.

------------------------------------------------
Listing all the elements that have not been completed

    ./todo.py ls

    This lists all elements, sorted by due date in descending order. There is also a number next to each element, this number is there to aid with completing an element.

------------------------------------------------
Completing a task

    ./todo.py do <number>

    Here, number refers to the number that is seen next to the elements when you run ./todo.py ls. Completing an element removes it completely, which is why I recommend having some form of version control (e.g. git) on the todo.txt file.
"""
        )
        return

    todolist = read_from_file(filename)

    if args[0] == "ls":
        todolist.sort(key=lambda e: e.duedate, reverse=True)
        for i, element in enumerate(todolist):
            print(f"{len(todolist) - i} {element}")

    elif args[0] == "add":
        element = TodoElement()
        element.from_input(*args[1:])
        todolist.append(element)

    elif args[0] == "do":
        index = len(todolist) - int(args[1])
        todolist.remove(todolist[index])

    write_to_file(filename, todolist)


if __name__ == "__main__":
    main()
