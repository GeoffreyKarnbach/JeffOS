class ROM:

    def __init__(self):
        self.memory = [0]*8192
    
    def getPosition(self, position):
        return self.memory[position]

    def setPosition(self, position, value):
        self.memory[position] = value
    
    def representation(self):
        for page in range(8):
            for row in range(16):
                for column in range(64):
                    print(self.memory[(1024*page)+(column + 64 * row)], end = " ")
                print()
            print()
            print()