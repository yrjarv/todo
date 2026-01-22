# Todo-CLI

A very, very simple CLI for manging a todolist. If you want synchronization, you will need to sync the `.txt` file with GitHub or a similar tool.

This is primarily made for myself, but I thought that maybe someone else needs an extremely minimal todo CLI, so I might as well share the code.

There is no way to restore completed tasks, so it is also probably best if you store the `.txt` file in a separate directory (the default is `todolist/todo.txt` relative to wherever the script is run, which means you have to run it from your home directory). Therefore, the absolute path to `todo.txt` file should be manually specified in the source code.

In order to make the file available from everywhere on the system, I recommend symlinking it to the `bin` directory: `ln -s ~/todo/todo.py /usr/bin/todo`.

## Usage

This can be found by running `./todo.py -h`.
