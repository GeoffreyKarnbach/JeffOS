from process import*

class Dispatcher:

    def __init__(self, processor):
        self.newQueue = []

        self.readyQueue = []
        self.suspendReadyQueue = []

        self.blockedQueue = []
        self.suspendBlockedQueue = []

        self.exitQueue = []

        self.running = None

        self.processor = processor
        self.currentCycle = 0

    def create_new_process(self, codefile):
        self.readyQueue.append(Process(codefile, self, self.processor))

    def round_robin(self):
        pass

    def run_next(self):
        print(self.currentCycle)
        self.currentCycle += 1
        
        if self.running is None:
            self.running = self.select_next_process()

        if self.running is not None:
            if self.running.hasNextOP():
                self.running.runNextOP()
                return True
            else:
                pass
        else:
            return False
    
    def select_next_process(self):
        if len(self.readyQueue) > 0:
            self.running = self.readyQueue.pop(0)
            return self.running
        
        return None

        

    #TODO: Implement Scheduling Algorithms

    #TODO: Short/Mid/Long Term Scheduling