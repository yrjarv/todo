# Todo-CLI

A very, very simple CLI for manging a todolist. If you want synchronization, you will need to sync the `.txt` file with GitHub or a similar tool.

There is no way to restore completed tasks, so it is also probably best if you store the `.txt` file in a separate directory (the default is `todolist/todo.txt` relative to wherever the script is run, which means you have to run it from your home directory). Therefore, the absolute path to `todo.txt` file should be manually specified in the source code.

In order to make the file available from everywhere on the system, I recommend symlinking it to the `bin` directory: `ln -s ~/todo/todo.py /usr/bin/todo`.

![image of use](/images/image.png)

## Usage

### Adding a new task

`./todo.py add <category> <name> <due date> <priority>`

`due date` is optional. If `due date` is not given, the current date is used. The format for the due date is `ddmmm`, e.g. `28feb`.

### Listing all the elements that have not been completed

`./todo.py ls`

This lists all elements, sorted by due date in descending order. There is also a number next to each element, this number is there to aid with completing an element.

### Completing a task

`./todo.py do <number>`

Here, `number` refers to the number that is seen next to the elements when you run `./todo.py ls`. Completing an element removes it completely, which is why I recommend having some form of version control (e.g. git) on the `todo.txt` file.
