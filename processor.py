from semaphore import*

class Processor:

    def __init__(self, RAM, ROM):
        self.registerA = 0
        self.registerB = 0
        self.registerC = 0
        self.registerD = 0
        self.registerE = 0
        self.registerF = 0
        self.registerG = 0
        self.registerH = 0

        self.translationTable = {"A":self.registerA,
                                 "B":self.registerB,
                                 "C":self.registerC,
                                 "D":self.registerD,
                                 "E":self.registerE,
                                 "F":self.registerF,
                                 "G":self.registerG,
                                 "H":self.registerH}

        self.ram = RAM
        self.rom = ROM

        self.negativeBit = False
        self.zeroBit = False

        self.semTable = {}
    
    def resetFlags(self):
        self.negativeBit = False
        self.zeroBit = False

    def setFlags(self, register = None):
        if register is not None:
            self.negativeBit = register < 0
            self.zeroBit = register == 0

    def getStatusBit(self):
        return [self.negativeBit, self.zeroBit]
    
    ##############################################

    def add(self, reg1, reg2, process):
        self.resetFlags()
        self.translationTable[reg1] += self.translationTable[reg2]
        self.setFlags(self.translationTable[reg1])
    
    def minus(self, reg1, reg2, process):
        self.resetFlags()
        self.translationTable[reg1] -= self.translationTable[reg2]
        self.setFlags(self.translationTable[reg1])
    
    def multiply(self, reg1, reg2, process):
        self.resetFlags()
        self.translationTable[reg1] *= self.translationTable[reg2]
        self.setFlags(self.translationTable[reg1])
    
    def jump(self, lineNB, process):
        process.setLine(int(lineNB))
        self.resetFlags()

    def jumpn(self, lineNB, process):
        if self.getStatusBit()[0]:
            process.setLine(int(lineNB))
        else:
            process.nextLine()
        self.resetFlags()

    def jumpz(self, lineNB, process):
        if self.getStatusBit()[1]:
            process.setLine(int(lineNB))
        else:
            process.nextLine()
        self.resetFlags()

    def load(self, reg, address, process):
        self.translationTable[reg] = self.ram.getPosition(int(address))
        self.resetFlags()
    
    def store(self, address, reg, process):
        self.ram.setPosition(int(address),self.translationTable[reg])
        self.resetFlags()
    
    def read(self, reg, address, process):
        self.translationTable[reg] = self.rom.getPosition(int(address))
        self.resetFlags()
    
    def write(self, address, reg, process):
        self.rom.setPosition(int(address),self.translationTable[reg])
        self.resetFlags()
    
    def init(self, sem, val, process):
        self.semTable[sem] = Semaphore(int(val))
        self.resetFlags()
    
    def semwait(self, sem, process):
        self.semTable[sem].wait(process)
        self.resetFlags()

    def sempost(self, sem, process):
        self.semTable[sem].post()
        self.resetFlags()