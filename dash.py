import shell
import rob


class Exit(shell.Command):
    manual = "Exits"
    syntax = "exit"

    def execute(self, args):
        print("Exiting...")
        exit(0)


class Hello(shell.Command):
    manual = "Hello world"
    syntax = "hello"

    def execute(self, args):
        print("Hello World!")


class Help(shell.Command):
    manual = "Prints all commands"
    syntax = "help"

    def execute(self, args):
        # Prints each key in commands on a new line
        keys = (dash_commands.keys())
        for key in keys:
            print(key)


class Man(shell.Command):
    manual = "Get's the manual for a given command"
    syntax = "man <command>"

    def execute(self, args):
        if len(args) > 1:
            print("Too many arguments")
            print("Usage: " + self.get_syntax())
            return

        for i in dash_commands.keys():
            if i == args[0]:
                print("Usage: " + dash_commands.get(i).get_syntax())
                print(dash_commands.get(i).get_man())
                return
        print("Could not find input command")

class SSH(shell.Command):
    manual = "Acts as a remote command module for accessing distinct networked systems."
    syntax = "ssh <destination-name>"

    def execute(self, args):
        if not args: return
        
        if(args[0] == "ssh@192.056.729:72301"):
           rob.rob_shell.main_loop()


dash_commands = {"exit": Exit(),
            "hello": Hello(),
            "help": Help(),
            "man": Man(),
            "ssh": SSH()
            }
