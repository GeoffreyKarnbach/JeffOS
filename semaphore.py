'''
Semaphore implementation, with process unblocking using FIFO method.
'''

class Semaphore:
    def __init__(self, value):
        self.value = value
        self.queue = []
    
    def wait(self, process):
        self.value -= 1
        if self.value < 0:
            self.queue.append(process)
            process.toBlockedQueue()

    def post(self):
        self.value += 1
        if self.value <= 0:
            process = self.queue.pop(0)
            process.toReadyQueue()