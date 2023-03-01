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

    def create_new_process(self, codefile):
        self.readyQueue.append(Process(codefile, self, self.processor))

    def round_robin(self):
        pass

    def run_next(self):
        try:
            self.readyQueue[0].runNextOP()
            return True
        except:
            return False
        

    #TODO: Implement Scheduling Algorithms

    #TODO: Short/Mid/Long Term Scheduling