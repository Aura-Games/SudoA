from abc import ABC, abstractmethod
import data


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


class Exit(Command):
    manual = "Exits"
    syntax = "exit"

    def execute(self, args):
        print("Exiting...")
        exit(0)


class Hello(Command):
    manual = "Hello world"
    syntax = "hello"

    def execute(self, args):
        print("Hello World!")


class Help(Command):
    manual = "Prints all commands"
    syntax = "help"

    def execute(self, args):
        # Prints each key in commands on a new line
        keys = (data.commands.keys())
        for key in keys:
            print(key)


class Man(Command):
    manual = "Get's the manual for a given command"
    syntax = "man <command>"

    def execute(self, args):
        if len(args) > 1:
            print("Too many arguments")
            print("Usage: " + self.get_syntax())
            return

        for i in data.commands.keys():
            if i == args[0]:
                print("Usage: " + data.commands.get(i).get_syntax())
                print(data.commands.get(i).get_man())
                return
        print("Could not find input command")
