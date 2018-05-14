import random as rd

class Backend(): # Definição da classe de BackEnd
    def __init__(self):
        self.pid = [] # Lista de processos
        self.pages = [] # Lista de Páginas
        self.frames = [-1, -1, -1, -1, -1, -1, -1, -1] # Lista de frames setado como default
        self.cont = 0 # Variável auxiliar de contador
        self.first = 0 # Variável usada para o FIFO
        self.actual = -1 # Variável que mostra a página atual
        self.frameActual = 0 # Variável que mostra o quadro atual
        self.missHit = [0, 0] # Lista de acerto/erro de página
 
    def createProcess(self, size): # Função que cria um processo
        self.pid.append([size, self.first, rd.randint(2, 8)])
        
    def setPages(self): # Função que determina quantas páginas cada processo necessita
        if(self.cont <= len(self.pid)):
            self.pages.append([])
            self.numberPages = (int(self.pid[self.cont][0]/2))

            for i in range(self.numberPages):
                self.pages[self.cont].append(-2)

            for i in range(self.numberPages, 6):
                self.pages[self.cont].append(-1)

            self.cont += 1
            self.first += 1

    def missAndHit(self): # Retorna a quantidade de PageMiss e PageHit
        return self.missHit

    def killProcess(self, pid): # Função que encerra um processo com base no seu PID
        try:
            pid = int(pid)
            for i in range(len(self.pid)):
                if(self.pid[i][1] == pid):
                    a = self.pid[i]
                    self.pid.remove(a)
                    a = self.pages[i]
                    self.pages.remove(a)
                    self.cont -= 1
                    if(self.actual > 0): 
                        self.actual -= 1
                    break
        except ValueError:
            print("Entre com um inteiro")

        if(len(self.pid) == 0):
            self.actual = 0
            self.cont = 0
            self.first = 0
            self.pages = []
            self.pid = []

    def getPids(self): # Função que retorna uma mini-fila de processos, com base no PID
        self.aux = self.actual+1
        if(self.actual == len(self.pid)-1):
            self.aux = 0

        if(len(self.pid) > 0):
            return [self.pid[self.actual-1][1],self.pid[self.actual][1], self.pid[self.aux][1]]
        else:
            return [-1,-1,-1]

    def setFrames(self): # Função que determina quem está usando qual quadro da memória  
        if(self.actual < len(self.pid)):
            self.pageSize = int(self.pid[self.actual][0]/2)
        
            for i in range(8):
                if(self.frames[i] == self.pid[self.actual][1]):
                    self.pageSize -= 1
                    self.missHit[0] += 1

            if(self.pageSize > 0):
                for i in range(self.pageSize):
                    self.pages[self.actual][i] = self.frameActual
                    self.frames[self.frameActual] = self.pid[self.actual][1]
                    self.frameActual += 1
                    self.missHit[1] += 1
                    if(self.frameActual == 8):
                        self.frameActual = 0

            return self.frames

    def actualPage(self): # Função que retorna a página atual
        self.pid[self.actual][2] -= 1
        if(self.pid[self.actual][2] == 0):
            self.killProcess(self.pid[self.actual][1])
        else:
            self.actual += 1

        if(self.actual >= len(self.pid)):
            self.actual = 0

        if(self.actual >= 0 and len(self.pages) > 0):
            print(str(self.actual) + "  " + str(len(self.pages)))
            return self.pages[self.actual]
        else:
            return [-1,-1,-1,-1,-1,-1]
    
    def quantPid(self): # Função que retorna a quantidade de processos na fila de execução
        return len(self.pid)
