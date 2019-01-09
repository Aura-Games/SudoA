import data


while True:
    # Get's a command input ignoring tabs and converting to a list
    user_input = input("$: ").replace("\t", " ").split(" ")
    # Converts to array of words
    user_input = [x for x in user_input if len(x) > 0]
    # print(command)

    if user_input:
        # Case insensitive
        user_input[0] = user_input[0].lower()

        # If word found, call it with parameters
        if user_input[0] in data.commands:
            command_object = data.commands[user_input[0]]
            command_object.execute(user_input[1:])
        else:
            print("Command not found!")
