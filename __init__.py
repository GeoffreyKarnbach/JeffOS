from process import*
from processor import*
from dispatcher import*
from ram import*
from rom import*

ram = RAM()
rom = ROM()

rom.setPosition(0, 49)
rom.setPosition(1, 1)

processor = Processor(ram, rom)

dispatcher = Dispatcher(processor)

dispatcher.create_new_process("Programs/ProgramD")

keep = True
while keep:
    keep = dispatcher.run_next()

rom.representation()

'''
TODO: 
1 Register?
-1 Register?

Direct Referencing of Register Value for writing to ROM/RAM => Indirect Address Referencing
Load value directly into Register => Direct Value Addressing for Register
'''