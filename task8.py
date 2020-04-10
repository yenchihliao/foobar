import math
from fractions import Fraction as frct

def vecMinus(a, b):
    ret = [0] * 2
    ret[0] = a[0] - b[0]
    ret[1] = a[1] - b[1]
    if(ret[1]):
        return frct(ret[0], ret[1]), ret
    elif(ret[0] > 0):
        return 1, ret
    else:
        return 0, ret

def bigger(a, b): # TODO
    pass

def shootPos(my_pos, target, result):
    f, ret = vecMinus(target, my_pos)
    if(f in result):
        if(bigger(result[f], ret)):
            result[f] = ret
    else:
        result[f] = ret
class allPositions:
    def __init__(self):
        self.

class BorderYByX:
    def __init__(self, width):
        width = width * 2 + 1
        self.posBorder = [0] * width
        self.negBorder = [0] * width
    def put(x, y, border):
    def get(x, y, border):

def solution(dimension, my_pos, guard_pos, distance):
# find all possible positions that can be shooted(me, guard, and corners)
    # LRMirrorX[whether in LRMirrorX][me or guard position] = the x coordinate
    # UDMirrorY[whether in UDMirrorY][me or guard position] = the y coordinate
    LRMirrorX = [[my_pos[0], guard_pos[0]], [dimension[0]-my_pos[0], dimension[0]-guard_pos[0]]]
    UDMirrorY = [[my_pos[1], guard_pos[1]], [dimension[1]-my_pos[1], dimension[1]-guard_pos[1]]]
    me2CornerInQuadrant = [[0] * 2]
    _, tmp = vecMinus(dimension, my_pos)
    me2CornerInQuadrant.append(tmp)
    _, tmp = vecMinus([0, dimension[1]], my_pos)
    me2CornerInQuadrant.append(tmp)
    _, tmp = vecMinus([0, 0], my_pos)
    me2CornerInQuadrant.append(tmp)
    _, tmp = vecMinus([dimension[0], 0], my_pos)
    me2CornerInQuadrant.append(tmp)
# find the border in mirror worlds that is guaranteed to be hit
    width = int(distance/dimension[0])
    border = BorderYByX(width)
    count = 0
    for i in range(width + 1):
    # x = count * dimension[0]
    # while(distance >= x):
    #     target = (distance + x) * (distance - x)
    #     yBorder.append(int(math.ceil(math.sqrt(target)/dimension[1])))
    #     count += 1
    #     x = count * dimension[0]
    # print(yBorder)
# find shootable guards ,non-shootable me, and non-shootable corners in mirror worlds
    # shoot at right hand side
    shootGuard = {}
    shootMyself = {}
    shootCorner = {} # TODO
    for xMirror in range(len(yBorder)):
        yMirror = -1 * yBorder[xMirror]
        while(yMirror < yBorder[xMirror]): # TODO: deal with border condition later
            target = [xMirror*dimension[0] + LRMirrorX[xMirror%2][1],
                    yMirror*dimension[1] + UDMirrorY[yMirror%2][1]] # Guard
            shootPos(my_pos, target, shootGuard)
            target = [xMirror*dimension[0] + LRMirrorX[xMirror%2][0],
                    yMirror*dimension[1] + UDMirrorY[yMirror%2][0]] # Me
            shootPos(my_pos, target, shootMyself)
            yMirror += 1
    print shootGuard.keys()

    # shoot at left hand side
    shootGuard2 = {}
    shootMyself2 = {}
    for xMirror in range(1, len(yBorder)):
        yMirror = -1 * yBorder[xMirror]
        while(yMirror < yBorder[xMirror]): # TODO: deal with border condition later
            target = [-1*xMirror*dimension[0] + LRMirrorX[-1*xMirror%2][1],
                    yMirror*dimension[1] + UDMirrorY[yMirror%2][1]] # Guard
            shootPos(my_pos, target, shootGuard2)
            target = [-1*xMirror*dimension[0] + LRMirrorX[-1*xMirror%2][0],
                    yMirror*dimension[1] + UDMirrorY[yMirror%2][0]] # Me
            shootPos(my_pos, target, shootMyself2)
            yMirror += 1
    print shootGuard2.keys()



if __name__ == '__main__':
    solution([3,2], [1,1], [2,1], 4)
    # solution([300,275], [150,150], [185,100], 500)
