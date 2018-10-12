def cmd_exit():
    print("Exiting...")
    exit(0)


def cmd_hello():
    print("Hello World!")


commands = {"exit": cmd_exit,
            "hello": cmd_hello}


while True:
    command = input("$: ")
    if command in commands:
        commands[command]()
    else:
        print("Command not found!")