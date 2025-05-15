# Todo-CLI

**WARNING**: This is not really maintained anymore, even though I use it daily. Therefore, this README might be quite out of sync with the real behaviour of the script.

A very, very simple CLI for manging a todolist. If you want synchronization, you will need to sync the `.txt` file with GitHub or a similar tool.

This is primarily made for myself, but I thought that maybe someone else needs an extremely minimal todo CLI, so I might as well share the code.

There is no way to restore completed tasks, so it is also probably best if you store the `.txt` file in a separate directory (the default is `todolist/todo.txt` relative to wherever the script is run, which means you have to run it from your home directory). Therefore, the absolute path to `todo.txt` file should be manually specified in the source code.

In order to make the file available from everywhere on the system, I recommend symlinking it to the `bin` directory: `ln -s ~/todo/todo.py /usr/bin/todo`.

![image of use](/images/image.png)

## Usage

### Adding a new task

`./todo.py add <category> <name> <due date> <priority>`

`due date` is optional. If `due date` is not given, the current date is used. The format for the due date is `ddmmm`, e.g. `28feb`.

### Listing all the elements that have not been completed

`./todo.py ls <amount>`

This lists all elements, sorted by due date in descending order. There is also a number next to each element, this number is there to aid with completing an element.

`amount` specifies how many elements to show, this argument is optional (defaults to 10).

### Completing a task

`./todo.py do <number>`

Here, `number` refers to the number that is seen next to the elements when you run `./todo.py ls`. Completing an element removes it completely, which is why I recommend having some form of version control (e.g. git) on the `todo.txt` file.

### Editing a task's name

`./todo.py editname <number> <name>`

Changing the name of the element with a specific number (see 'Completing a task') to `name`.

### Editing a task's date

`./todo.py editdate <number> <date>`

Changing the date, just as with `editname`. `date` is a date on the same format as when you add a new element.

### Editing which category a task is in

`./todo.py editcat <number> <category>`

Changing the category
