from Queue import Queue
from copy import deepcopy

class Check():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.limit = width + height - 1
    def up(self, pos):
        return pos.x > 0
    def down(self, pos):
        return pos.x < self.height - 1
    def left(self, pos):
        return pos.y > 0
    def right(self, pos):
        return pos.y < self.width - 1
    def perfect(self, maze):
        return maze[self.height-1][self.width-1] == self.limit

class MazeInfo():
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count

def distCount(maze, checker, x, y):
    BFS = Queue(400)
    BFS.put(MazeInfo(x, y, 1))
    while(not BFS.empty()):
        cur = BFS.get()
        if(maze[cur.x][cur.y] != 0):
            continue
        maze[cur.x][cur.y] = cur.count
        if(checker.up(cur)):
            if(maze[cur.x-1][cur.y] == 0):
                BFS.put(MazeInfo(cur.x-1, cur.y, cur.count+1))
            elif(maze[cur.x-1][cur.y] == 1):
                maze[cur.x-1][cur.y] = -1*cur.count
        if(checker.down(cur)):
            if(maze[cur.x+1][cur.y] == 0):
                BFS.put(MazeInfo(cur.x+1, cur.y, cur.count+1))
            elif(maze[cur.x+1][cur.y] == 1):
                maze[cur.x+1][cur.y] = -1*cur.count
        if(checker.left(cur)):
            if(maze[cur.x][cur.y-1] == 0):
                BFS.put(MazeInfo(cur.x, cur.y-1, cur.count+1))
            elif(maze[cur.x][cur.y-1] == 1):
                maze[cur.x][cur.y-1] = -1*cur.count
        if(checker.right(cur)):
            if(maze[cur.x][cur.y+1] == 0):
                BFS.put(MazeInfo(cur.x, cur.y+1, cur.count+1))
            elif(maze[cur.x][cur.y+1] == 1):
                maze[cur.x][cur.y+1] = -1*cur.count
    maze[x][y] = 1
    # viewMaze(maze)

def solution(maze):
    checker = Check(len(maze), len(maze[0]))
    # viewMaze(maze)
    mazeFromEnd = deepcopy(maze)
    distCount(maze, checker, 0, 0)
    if(checker.perfect(maze)):
        return checker.limit
    distCount(mazeFromEnd, checker, len(maze)-1, len(maze[0])-1)
    shortestCut = 400
    for i in range(checker.height):
        for j in range(checker.width):
             if(maze[i][j] < 0 and mazeFromEnd[i][j] < 0):
                 tmp = -1 * (maze[i][j] + mazeFromEnd[i][j]) + 1
                 if(tmp < shortestCut):
                     if(tmp == checker.limit):
                         return tmp
                     else:
                         shortestCut = tmp
    return shortestCut

def viewMaze(maze):
    for row in maze:
        for num in row:
            print '%5d'%num,
        print('')
    print('-------------')

import random
from time import time
if __name__ == '__main__':
    maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(solution(maze))
    maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print(solution(maze))
    # maze = [
    # [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    # [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]
    # print(solution(maze))
    # [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    # [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    # [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    # [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    # [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    # [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    # [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    # [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]
    # maze = []
    # for i in range(10):
    #     tmp = []
    #     for j in range(10):
    #         if(random.random() > 0.7):
    #             tmp.append(1)
    #         else:
    #             tmp.append(0)
    #     maze.append(deepcopy(tmp))
    # maze[0][0] = 0
    # maze[-1][-1] = 0
    # print(solution(maze))
