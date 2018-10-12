import state

# Functions
def cmd_rob(args):
    if args:
        if args[0] in commands:
            commands[args[0]](args[1:])
        else:
            print("Invalid choice")
    else:
        print("Robot doesn't actually do anything without scout - sorry")


def cmd_rob_scout(args):
    if args:
        try:
            planet_id = int(args[0])
            if 0 <= planet_id < len(state.world.planet_richness):
                print("Found a "+str(float.__round__(state.world.planet_richness[planet_id]*100))+"% richness planet")
            else:
                print("Invalid planet-id: out of range")
        except ValueError:
            print("Invalid planet-id: must be an integer")
    else:
        print("Usage: rob scout [planet-id]")


# Not Functions
commands = {"scout": cmd_rob_scout}