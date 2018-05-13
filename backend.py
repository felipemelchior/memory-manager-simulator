import random as rd

class Backend():
    def __init__(self):
        self.pid = []
        self.pages = []
        self.frames = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.cont = 0
        self.actual = -1
        self.first = 0

    def createProcess(self, size):
        self.pid.append([size, len(self.pid), rd.randint(1, 10)])
        
    def setPages(self):
        self.numberPages = (int(self.pid[self.cont][0]/2))

        self.pages.append([])

        for i in range(self.numberPages):
            self.pages[self.cont].append("*")

        for i in range(self.numberPages, 6):
            self.pages[self.cont].append(-1)

        self.cont += 1

    def actualPage(self):
        self.actual += 1
        return self.pages[self.actual]
        



    

