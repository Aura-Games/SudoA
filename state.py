import random


class World:
    def __init__(self):
        self.planet_richness = [random.random() for i in range(5)]


world = World()