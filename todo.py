#!/usr/bin/env python3
"""Python program to manage a todolist"""

import os
import argparse
import datetime


class TodoElement:
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

    def from_input(self, category: str, name: str, duedate: str) -> None:
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
    todolist = read_from_file(filename)

    parser = argparse.ArgumentParser(
            prog="todo",
            description="Simple CLI for a simple todolist"
    )
    verbParsers = parser.add_subparsers(dest="verb")
    addParser = verbParsers.add_parser("add")
    addParser.add_argument("category")
    addParser.add_argument("name")
    addParser.add_argument("due_date", nargs="?",
                           default=datetime.datetime.today().date().strftime("%d%b"))
    lsParser = verbParsers.add_parser("ls")
    lsParser.add_argument("number", type=int, nargs="?", default=len(todolist))
    doParser = verbParsers.add_parser("do")
    doParser.add_argument("number", type=int)
    editParser = verbParsers.add_parser("edit")
    editParser.add_argument("number", type=int)
    editParsers = editParser.add_subparsers(dest="field")
    editNameParser = editParsers.add_parser("name")
    editNameParser.add_argument("name")
    editDateParser = editParsers.add_parser("date")
    editDateParser.add_argument("date", nargs="?",
                                default=str(datetime.datetime.today().date()))
    editCategoryParser = editParsers.add_parser("category")
    editCategoryParser.add_argument("category")

    args = parser.parse_args()


    match args.verb:
        case "add":
            element = TodoElement()
            element.from_input(args.category, args.name, args.due_date)
            todolist.append(element)
        case "ls":
            if args.number > len(todolist):
                args.number = len(todolist)
            from_index = len(todolist) - args.number + 1
            todolist.sort(key = lambda e: e.duedate, reverse=True)
            for i, element in enumerate(todolist[from_index - 1:]):
                print(f"{len(todolist) - from_index - i + 1:3} {element}")
        case "do":
            todolist.remove(todolist[len(todolist) - args.number])
        case "edit":
            index = len(todolist) - args.number
            match args.field:
                case "name":
                    todolist[index].name = args.name
                case "date":
                    todolist[index].duedate = datetime.datetime.strptime(
                        f"{args.date}{datetime.datetime.today().year}", "%d%b%Y"
                    ).date()

                case "category":
                    todolist[index].category = args.category
            
    write_to_file(filename, todolist)

if __name__ == "__main__":
    main()
