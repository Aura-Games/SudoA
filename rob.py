import state
import shell


'''def cmd_rob_scout(args):
    if args:
        try:
            planet_id = int(args[0])
            if 0 <= planet_id < len(state.world.planet_richness):
                print("Found a " + str(
                    float.__round__(state.world.planet_richness[planet_id] * 100)) + "% richness planet")
            else:
                print("Invalid planet-id: out of range")
        except ValueError:
            print("Invalid planet-id: must be an integer")
    else:
        print("Usage: rob scout [planet-id]")


# Commands List
commands = {"scout": cmd_rob_scout}


def get_subcommands_as_string():
    # Prints each key in commands on a new line
    keys = (commands.keys())
    string = ""
    for key in keys:
        if string is not "":
            string += ", "
        string += key
    return string


class Rob(shell.Command):
    manual = "Gives a robot the command specified\n" \
             "Subcommands: " + get_subcommands_as_string()
    syntax = "rob <subcommand>"

    def execute(self, args):
        if args:
            if args[0] in commands:
                commands[args[0]](args[1:])
            else:
                print("Invalid choice")
        else:
            print("Robot doesn't actually do anything without scout - sorry")
'''


class Scout(shell.Command):
    manual = "Sends the robot to the specified planet"
    syntax = "scout <planet-id>"

    def execute(self, args):
        if args:
            try:
                planet_id = int(args[0])
                if 0 <= planet_id < len(state.world.planet_richness):
                    print("Found a " + str(
                        float.__round__(state.world.planet_richness[planet_id] * 100)) + "% richness planet")
                else:
                    print("Invalid planet-id: out of range")
            except ValueError:
                print("Invalid planet-id: must be an integer")
        else:
            print("Usage: " + self.syntax)


rob_commands = {"scout": Scout()}

rob_shell = shell.ShellEnvironment("192.056.729", rob_commands)
