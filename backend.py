import random as rd

class Backend():
    def __init__(self):
        self.pid = []
        self.pages = []
        self.frames = []

    def createProcess(self, size):
        self.pid.append((size, len(self.pid), rd.randint(1, 10)))

    def setPages(self):
        

