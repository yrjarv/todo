#!/usr/bin/python3
"""Python program to manage a todolist"""

import sys
import os
import datetime


class TodoElement:
    """Todo Element"""

    def __init__(self):
        self.category: str = ""
        self.name: str = ""
        self.duedate: datetime.date = datetime.datetime.today().date()

    def from_storage(self, string: str) -> None:
        string_elements: list[str] = string.split(";")
        if len(string_elements) != 3:
            raise ValueError("Invalid string length: " + string)

        self.category = string_elements[0]
        self.name = string_elements[1]

        year, month, day = (int(element) for element in string_elements[2].split("-"))
        self.duedate = datetime.date(year, month, day)

    def to_storage(self) -> str:
        return f"{self.category};{self.name};{self.duedate}"

    def from_input(self, category: str, name: str, duedate: str = "") -> None:
        self.category = category
        self.name = name

        if duedate == "":
            self.duedate = datetime.datetime.today().date()
        else:
            try:
                self.duedate = datetime.datetime.strptime(
                    f"{duedate}{datetime.datetime.today().year}", "%d%b%Y"
                ).date()
            except ValueError as e:
                raise ValueError("Invalid date: " + duedate, e)

    def __str__(self) -> str:
        return f"{self.duedate}: {self.category} {self.name}"


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
    filename = os.path.expanduser("~/todolist/todo.txt")
    args = sys.argv[1:]

    if len(args) == 0:
        print(
            """
Usage

./todo.py add <category> <name> <due date> <priority>
    `due date` is optional. If `due date` is not given, the current date is
    used. The format for the due date is `ddmmm`, e.g. `28feb`.

`./todo.py ls <amount>`
    Lists all elements, sorted by due date in descending order.
    `amount` specifies how many elements to show, this argument is optional
        (defaults to showing all)

`./todo.py do <number>`

`./todo.py editname <number> <name>`

`./todo.py editdate <number> <date>`

`./todo.py editcat <number> <category>`
"""
        )
        return

    todolist = read_from_file(filename)

    if args[0] == "ls":
        if len(args) > 1:
            amount = int(args[1])
        else:
            amount = len(todolist)

        if amount > len(todolist):
            amount = len(todolist)

        from_index = len(todolist) - amount + 1

        todolist.sort(key=lambda e: e.duedate, reverse=True)
        for i, element in enumerate(todolist[from_index - 1:]):
            print(f"{len(todolist) - from_index - i + 1:3} {element}")

    elif args[0] == "add":
        element = TodoElement()
        element.from_input(*args[1:])
        todolist.append(element)

    elif args[0] == "do":
        index = len(todolist) - int(args[1])
        todolist.remove(todolist[index])

    elif args[0] == "editname":
        index = len(todolist) - int(args[1])
        todolist[index].name = args[2]

    elif args[0] == "editdate":
        index = len(todolist) - int(args[1])
        element = todolist[index]
        duedate = args[2]
        if duedate == "":
            element.duedate = datetime.datetime.today().date()
        else:
            try:
                element.duedate = datetime.datetime.strptime(
                    f"{duedate}{datetime.datetime.today().year}", "%d%b%Y"
                ).date()
            except ValueError as e:
                raise ValueError("Invalid date: " + duedate, e)

    elif args[0] == "editcat":
        index = len(todolist) - int(args[1])
        todolist[index].category = args[2]

    write_to_file(filename, todolist)


if __name__ == "__main__":
    main()
