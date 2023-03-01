class RAM:

    def __init__(self):
        self.memory = [0]*1024
    
    def getPosition(self, position):
        return self.memory[position]

    def setPosition(self, position, value):
        self.memory[position] = value
    
    def representation(self):
        for row in range(16):
            for column in range(64):
                print(self.memory[column + 64 * row], end = " ")
            print()