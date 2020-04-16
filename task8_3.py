import math
from fractions import Fraction as frct

def vecMinus(a, b):
    ret = [0] * 2
    ret[0] = a[0] - b[0]
    ret[1] = a[1] - b[1]
    if(ret[1]):
        return frct(ret[0], ret[1]), ret
    elif(ret[0] > 0):
        return 1, ret # shooting vertically
    elif(ret[0] < 0):
        return -1, ret # shooting vertically
    else:
        return 0, ret # suicide

def bigger(a, b):
    if(a[0] == b[0]):
        return abs(a[1]) > abs(b[1])
    return abs(a[0]) > abs(b[0])

def tryShootPos(my_pos, target, result, distance):
    f, ret = vecMinus(target, my_pos)
    # print 'try shooting', target, ret
    if(ret[0]**2 + ret[1]**2 > distance**2):
        return False
    if(f in result):
        if(bigger(result[f], ret)):
            result[f] = ret
    else:
        result[f] = ret
    return True

class allPositions:
    def __init__(self, dimension, my_pos, guard_pos):
        # LRMirrorX[whether in LRMirrorX][me or guard position] = the x coordinate
        # UDMirrorY[whether in UDMirrorY][me or guard position] = the y coordinate
        self.LRMirrorX = [[my_pos[0], guard_pos[0]], [dimension[0]-my_pos[0], dimension[0]-guard_pos[0]]]
        self.UDMirrorY = [[my_pos[1], guard_pos[1]], [dimension[1]-my_pos[1], dimension[1]-guard_pos[1]]]
        self.me2CornerInQuadrant = [[0] * 2]
        _, tmp = vecMinus(dimension, my_pos)
        self.me2CornerInQuadrant.append(tmp)
        _, tmp = vecMinus([0, dimension[1]], my_pos)
        self.me2CornerInQuadrant.append(tmp)
        _, tmp = vecMinus([0, 0], my_pos)
        self.me2CornerInQuadrant.append(tmp)
        _, tmp = vecMinus([dimension[0], 0], my_pos)
        self.me2CornerInQuadrant.append(tmp)
        self.dimension = dimension
    def getMe(self, x, y):
        return [x * self.dimension[0] + self.LRMirrorX[x%2][0], y * self.dimension[1] + self.UDMirrorY[y%2][0]]
    def getGuard(self, x, y):
        return [x * self.dimension[0] + self.LRMirrorX[x%2][1], y * self.dimension[1] + self.UDMirrorY[y%2][1]]
    def getCorner(self, x, y, quadrant):
        return [x * self.dimension[0] + self.me2CornerInQuadrant[quadrant][0], y * self.dimension[1] + self.me2CornerInQuadrant[quadrant][1] ]

def solution(dimension, my_pos, guard_pos, distance):
    positions = allPositions(dimension, my_pos, guard_pos)
# find shootable guards ,non-shootable me, and non-shootable corners in mirror worlds
    shootGuardUpper = {}
    shootMyselfUpper = {}
    shootGuardLower = {}
    shootMyselfLower = {}
    Xborder = int(math.ceil(distance / dimension[0])) + 2
    Yborder = int(math.ceil(distance / dimension[0])) + 2
    for xMirror in range(-1 * Xborder, Xborder):
        for yMirror in range(Yborder + 1):
                tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
                tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
                tryShootPos(my_pos, positions.getCorner(xMirror, yMirror, 2), shootMyselfUpper, distance)
                tryShootPos(my_pos, positions.getCorner(xMirror, yMirror, 1), shootMyselfUpper, distance)
        for yMirror in range(-1 * Yborder, 0):
                tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
                tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)
                tryShootPos(my_pos, positions.getCorner(xMirror, yMirror, 3), shootMyselfLower, distance)
                tryShootPos(my_pos, positions.getCorner(xMirror, yMirror, 4), shootMyselfLower, distance)
        shootPos(my_pos, positions.getCorner(xMirror, 0, 3), shootMyselfLower, distance)
        shootPos(my_pos, positions.getCorner(xMirror, 0, 4), shootMyselfLower, distance)


    check = set(shootMyselfUpper) & set(shootGuardUpper)
    for key in check:
        if(bigger(shootGuardUpper[key], shootMyselfUpper[key])):
            shootGuardUpper.pop(key)
    check = set(shootMyselfLower) & set(shootGuardLower)
    for key in check:
        if(bigger(shootGuardLower[key], shootMyselfLower[key])):
            shootGuardLower.pop(key)
    print shootGuardUpper
    print shootGuardLower
    return len(set(shootGuardUpper)) + len(set(shootGuardLower))
if __name__ == '__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
