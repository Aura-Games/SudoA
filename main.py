import rob, state


def cmd_exit(args):
    print("Exiting...")
    exit(0)


def cmd_hello(args):
    print("Hello World!")


commands = {"exit": cmd_exit,
            "hello": cmd_hello,
            "rob": rob.cmd_rob}

while True:
    command = input("$: ").replace("\t", " ").split(" ")
    command = [x for x in command if len(x)>0]
    # print(command)

    if command:

        command[0] = command[0].lower()

        if command[0] in commands:
            commands[command[0]](command[1:])
        else:
            print("Command not found!")