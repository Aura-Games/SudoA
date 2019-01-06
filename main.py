import rob, state


def cmd_exit(args):
    print("Exiting...")
    exit(0)


def cmd_hello(args):
    print("Hello World!")


def cmd_help(args):
    # Prints each key in commands on a new line
    keys = (commands.keys())
    for key in keys:
        print(key)


# Possible commands and associated functions
commands = {"exit": cmd_exit,
            "hello": cmd_hello,
            "rob": rob.cmd_rob,
            "help": cmd_help}


while True:
    # Get's a command input ignoring tabs and converting to a list
    command = input("$: ").replace("\t", " ").split(" ")
    # Converts to array of words
    command = [x for x in command if len(x) > 0]
    # print(command)

    if command:
        # Case insensitive
        command[0] = command[0].lower()

        # If word found, call it with parameters
        if command[0] in commands:
            commands[command[0]](command[1:])
        else:
            print("Command not found!")
