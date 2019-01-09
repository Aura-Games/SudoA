import rob
import command


# Possible commands and associated functions
commands = {"exit": command.Exit(),
            "hello": command.Hello(),
            "rob": rob.Rob(),
            "help": command.Help(),
            "man": command.Man()}


