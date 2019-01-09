from abc import ABC, abstractmethod
import random


class ShellEnvironment():
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands
    
    def main_loop(self):
        while True:
            # Get's a command input ignoring tabs and converting to a list
            user_input = input(self.name+": ").replace("\t", " ").split(" ")
            # Converts to array of words
            user_input = [x for x in user_input if len(x) > 0]
            # print(command)

            if user_input:
                # Case insensitive
                user_input[0] = user_input[0].lower()

                # If word found, call it with parameters
                if user_input[0] in self.commands:
                    command_object = self.commands[user_input[0]]
                    command_object.execute(user_input[1:])
                else:
                    print("Command not found!")

    @staticmethod
    def generate_ip():
        rand_strs = [str(random.randint(0, 999)) for i in range(4)]
        return rand_strs[0] + "." + rand_strs[1] + "."  + rand_strs[2] + "."  + rand_strs[3]


class Command(ABC):
    manual = "This command has no manual"
    syntax = "Unknown"

    @abstractmethod
    def execute(self, args):
        pass

    def get_man(self):
        return self.manual

    def get_syntax(self):
        return self.syntax
