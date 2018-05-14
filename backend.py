import random as rd

class Backend():
    def __init__(self):
        self.pid = []
        self.pages = []
        self.frames = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.cont = 0
        self.count = 0
        self.actual = -1
        self.first = 0
        self.missHit = [1, 1]

    def createProcess(self, size):
        self.pid.append([size, self.count, rd.randint(1, 10)])
        
    def setPages(self):
        self.pages.append([])
        self.numberPages = (int(self.pid[self.cont][0]/2))

        for i in range(self.numberPages):
            self.pages[self.cont].append(-2)

        for i in range(self.numberPages, 6):
            self.pages[self.cont].append(-1)

        self.cont += 1
        self.count += 1

    def missAndHit(self):
        return self.missHit

    def killProcess(self, pid):
        try:
            pid = int(pid)
            if(pid >= 0 and pid < len(self.pid)):
                a = self.pid[pid]
                self.pid.remove(a)
                a = self.pages[pid]
                self.pages.remove(a)
                self.actual = 0
                self.cont -= 1
        except ValueError:
            print("Entre com um inteiro")

    def getPids(self):
        self.aux = self.actual+1
        if(self.actual == len(self.pid)-1):
            self.aux = 0

        return [self.pid[self.actual-1][1],self.pid[self.actual][1], self.pid[self.aux][1]]

    def setFrames(self):  
        self.pageSize = len(self.pages[self.actual])

        return self.frames

    def actualPage(self):
        self.actual += 1

        if(self.actual >= len(self.pid)):
            self.actual = 0
        
        return self.pages[self.actual]
    