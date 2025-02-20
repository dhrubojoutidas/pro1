class Shrimp():
    time2hatch = 4
    states = ["egg","adult"]
    
    def __init__(self, pos, mapSize):
        # The position of the shrimp as x & y values stored in a list
        self.pos = pos
        # All shrimp start as an egg and 0 years (timesteps) old
        self.state = self.states[0]
        self.age = 0
        self.mapSize = mapSize
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    def stepChange(self):
        self.age += 1
        # If the shrimp is an egg move down 10 steps
        if self.state == "egg":
            self.pos[1] -= 10
            # A egg becomes an adult after 4 timesteps
            if self.age > self.time2hatch:
                self.state = "adult"
        else:
            # If the shrimp is an adult move up 10 steps and right 10 steps
            self.pos[0] += 10
            self.pos[1] += 10

        # If the shrimp moved off the map, move it back on
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]
                        
    def getSize(self):
        # Shrimp eggs are smaller than adult shrimp
        if self.state == "egg":
            size = 5
        else:
            size = 15
        return size