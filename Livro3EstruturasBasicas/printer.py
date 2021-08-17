from DataStructuresChapter3.Queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStam(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)
        
        labPrinter.tick()

    averageWait = sum(waitingTimes)/len(waitingTimes)
    print(f"Average Wait {averageWait: 6.2f} secs {printQueue.size(): 3d} tasks remaining.")
    return averageWait, printQueue.size()

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

waitAverage = []
tasksUndone = []

for i in range(10):
    wait, tasks = simulation(3600, 10)
    waitAverage.append(wait)
    tasksUndone.append(tasks)

minWait = min(waitAverage)
maxWait = max(waitAverage)
finalWaitAverage = sum(waitAverage)/len(waitAverage)
tasksUndoneAverage = sum(tasksUndone)/len(tasksUndone)

print(f"Tempo médio de espera dos 10 testes: {finalWaitAverage: 6.2f} segundos.")
print(f"{minWait:0.2f} segundos foi o mínimo e {maxWait:0.2f} segundos foi o máximo de espera.")
print(f"Média de tarefas de impressão que não foram feitas: {tasksUndoneAverage: 6.2f}.")