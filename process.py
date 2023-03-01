class Process:
    currentPID = 1

    def __init__(self, codefile, dispatcher, processor):

        self.id = self.currentPID
        self.dispatcher = dispatcher
        self.processor = processor
        Process.currentPID += 1

        self.currentLine = 0
        self.code = self.fetch_program_code(codefile)

        print(self.code)
        
    def fetch_program_code(self, codefile):
        with open(codefile, "r") as f:
            content = f.read()
        
        content = content.strip()
        if "====\n" in content:
            content = content.split("====\n")[1]
        
        commands = []

        for line in content.split("\n"):

            currentLine = line.split(" | ")[1]
            currentLine = currentLine.strip()
            operation = currentLine.split(" ")[0]
            values = currentLine.split(" ")[1].split(",")

            commands.append([operation, values])

        return commands
    
    def toBlockedQueue(self):
        pass

    def toReadyQueue(self):
        pass

    def setLine(self, lineNB):
        self.currentLine = lineNB
    
    def nextLine(self):
        self.currentLine += 1

    def runNextOP(self):
        currentOPs = self.code[self.currentLine]

        if currentOPs[0] == "ADD":
            self.processor.add(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "MINUS":
            self.processor.minus(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "MULTIPLY":
            self.processor.multiply(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "JUMP":
            self.processor.jump(currentOPs[1][0], self)
        elif currentOPs[0] == "JUMPN":
            self.processor.jumpn(currentOPs[1][0], self)
        elif currentOPs[0] == "JUMPZ":
            self.processor.jumpz(currentOPs[1][0], self)
        elif currentOPs[0] == "LOAD":
            self.processor.load(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "STORE":
            self.processor.store(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "READ":
            self.processor.read(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "WRITE":
            self.processor.write(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "INIT":
            self.processor.init(currentOPs[1][0], currentOPs[1][1], self)
            self.currentLine += 1
        elif currentOPs[0] == "SEMWAIT":
            self.processor.semwait(currentOPs[1][0], self)
            self.currentLine += 1
        elif currentOPs[0] == "SEMPOST":
            self.processor.sempost(currentOPs[1][0], self)
            self.currentLine += 1
