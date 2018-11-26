from Base import *
from Direction import *
from queue import Queue
from time import *

class BFS:

    frontier = Queue()
    explored = {}

    def __init__(self, start, target, strategy):
        self.target = target
        self.start = Base(None, start, Direction(1), 0)
        self.strategy = strategy
        self.maxDepth = 0
        if(self.start.state != self.target):
            self.frontier.put(self.start.state)
            self.explored[str(self.start.state)] = self.start

    def solve(self):
        startTime = time()
        while(self.frontier.qsize() > 0):
            self.currentState = self.frontier.get()
            self.currentState = self.explored[str(self.currentState)]
            moves = self.currentState.getOrderedMoves(self.strategy)
            for move in moves:
                newState = Base(self.currentState, self.currentState.move(move), move, self.currentState.pathCost + 1)
                if(newState.pathCost > self.maxDepth):
                    self.maxDepth = newState.pathCost
                if(newState.state == self.target):
                    solvingTime = time() - startTime
                    return newState.getPath(), len(self.explored) + 1, len(self.explored) - self.frontier.qsize(), self.maxDepth, solvingTime
                if(str(newState.state) not in self.explored.keys()):
                    self.frontier.put(newState.state)
                    self.explored[str(newState.state)] = newState