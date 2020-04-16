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

def shootPos(my_pos, target, result):
    f, ret = vecMinus(target, my_pos)
    # print 'shooting', target, ret
    if(f in result):
        if(bigger(result[f], ret)):
            result[f] = ret
    else:
        result[f] = ret

def tryShootPos(my_pos, target, result, distance):
    f, ret = vecMinus(target, my_pos)
    # print 'try shooting', target, ret
    if(ret[0]**2 + ret[1]**2 > distance**2):
        return
    if(f in result):
        if(bigger(result[f], ret)):
            result[f] = ret
    else:
        result[f] = ret

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
    # print(dimension, my_pos, guard_pos, distance)
    # find all possible positions that can be shooted(me, guard, and corners)
    positions = allPositions(dimension, my_pos, guard_pos)

    # find the border in mirror worlds that is guaranteed to be hit
    # minX = int(math.ceil((distance - my_pos[0]) / dimension[0]))
    # maxX = int(math.ceil((distance - dimension[0] + my_pos[0])/dimension[0]))
    minX = (distance - my_pos[0]) // dimension[0]
    maxX = (distance - dimension[0] + my_pos[0]) // dimension[0]
    minUpperMiss = False
    minLowerMiss = False
    maxUpperMiss = False
    maxLowerMiss = False
    # The guaranteed borders between [-minX...-1, 0, 0, 1,...maxX]
    # Note that 0 appears twice
    upperBorder = []
    lowerBorder = []
    for x in range(-1 * minX, 1):
        x_dis = my_pos[0] - x * dimension[0]
        y_dis = math.sqrt((distance + x_dis) * (distance - x_dis))
        y_dis -= dimension[1] - my_pos[1]
        if(y_dis < 0):
            minUpperMiss = True
        else:
            upperBorder.append(int(y_dis//dimension[1]))
        y_dis += dimension[1] - my_pos[1] * 2
        if(y_dis < 0):
            minLowerMiss = True
        else:
            lowerBorder.append(int(y_dis//dimension[1]))
    for x in range(0, maxX + 1):
        x_dis = (x + 1) * dimension[0] - my_pos[0]
        y_dis = math.sqrt((distance + x_dis) * (distance - x_dis))
        y_dis -= dimension[1] - my_pos[1]
        if(y_dis < 0):
            maxUpeerMiss = True
        else:
            upperBorder.append(int(y_dis//dimension[1]))
        y_dis += dimension[1] - my_pos[1] * 2
        if(y_dis < 0):
            maxLowerMiss = True
        else:
            lowerBorder.append(int(y_dis//dimension[1]))

    # print(minX, maxX)
    # print(upperBorder, lowerBorder)

# find shootable guards ,non-shootable me, and non-shootable corners in mirror worlds
    # shoot at right hand side
    shootGuardUpper = {}
    shootMyselfUpper = {}
    shootGuardLower = {}
    shootMyselfLower = {}
    count = 0
    for xMirror in range(-1 * minX, 1):
        # print xMirror
        # deal with 2nd quadrant
        if(not minUpperMiss or xMirror != -1 * minX):
            for yMirror in range(upperBorder[count] + 1):
                # print '##', yMirror
                shootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper)
                shootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper)
                shootPos(my_pos, positions.getCorner(xMirror, yMirror, 2), shootMyselfUpper)
            if(xMirror != 0):
                for yMirror in range(upperBorder[count] + 1, upperBorder[count+1] + 2):
                    tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
                    tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
            yMirror = upperBorder[count] + 1
            tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
            tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
        # deal with 3rd quadrant
        if(not minLowerMiss or xMirror != -1 * minX):
            for tmpYMirror in range(lowerBorder[count] + 1):
                yMirror = tmpYMirror * -1
                # print '##', yMirror
                if(yMirror != 0):
                    shootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower)
                    shootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower)
                shootPos(my_pos, positions.getCorner(xMirror, yMirror, 3), shootMyselfLower)
            if(xMirror != 0):
                for tmpYMirror in range(lowerBorder[count] + 1, lowerBorder[count+1] + 2):
                    yMirror = tmpYMirror * -1
                    tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
                    tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)
            yMirror = -1 * (lowerBorder[count] + 1)
            tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
            tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)
        count += 1
    # patch the possible miss
    # print 'patching'
    if(not minUpperMiss):
        xMirror = -1 * minX - 1
    else:
        xMirror = -1 * minX
    for yMirror in range(upperBorder[0] + 2):
        tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
        tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
    if(not minLowerMiss):
        xMirror = -1 * minX - 1
    else:
        xMirror = -1 * minX
    for tmpYMirror in range(lowerBorder[0] + 2):
        if(minUpperMiss == minLowerMiss and tmpYMirror == 0):
            continue
        yMirror = -1 * tmpYMirror
        tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
        tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)

    count = 0
    for xMirror in range(maxX + 1):
        # print xMirror
        # deal with 1st quadrant
        if(not maxUpperMiss or xMirror != maxX):
            for yMirror in range(upperBorder[count] + 1):
                # print '##', yMirror
                shootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper)
                shootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper)
                shootPos(my_pos, positions.getCorner(xMirror, yMirror, 1), shootMyselfUpper)
            if(xMirror != 0):
                for yMirror in range(upperBorder[count] + 1, upperBorder[count-1] + 2):
                    tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
                    tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
            yMirror = upperBorder[count] + 1
            tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
            tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
        # deal with 4th quadrant
        if(not maxLowerMiss or xMirror != maxX):
            for tmpYMirror in range(lowerBorder[count] + 1):
                yMirror = tmpYMirror * -1
                # print '##', yMirror
                if(yMirror != 0):
                    shootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower)
                    shootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower)
                shootPos(my_pos, positions.getCorner(xMirror, yMirror, 4), shootMyselfLower)
            if(xMirror != 0):
                for tmpYMirror in range(lowerBorder[count] + 1, lowerBorder[count-1] + 2):
                    yMirror = tmpYMirror * -1
                    tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
                    tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)
            yMirror = -1 * (lowerBorder[count] + 1)
            tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
            tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)
        count += 1
    # patch the possible miss
    # print 'patching'
    if(not maxUpperMiss):
        xMirror = maxX + 1
    else:
        xMirror = maxX
    for yMirror in range(upperBorder[-1] + 2):
        tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardUpper, distance)
        tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfUpper, distance)
    if(not maxLowerMiss):
        xMirror = maxX + 1
    else:
        xMirror = maxX
    for tmpYMirror in range(lowerBorder[-1] + 2):
        if(maxUpperMiss == maxLowerMiss and tmpYMirror == 0):
            continue
        yMirror = -1 * tmpYMirror
        tryShootPos(my_pos, positions.getGuard(xMirror, yMirror), shootGuardLower, distance)
        tryShootPos(my_pos, positions.getMe(xMirror, yMirror), shootMyselfLower, distance)

    # print(shootGuardUpper)
    # print(shootGuardLower)
    # print(shootMyselfLower)
    # print(shootMyselfUpper)

    check = set(shootMyselfUpper) & set(shootGuardUpper)
    for key in check:
        if(bigger(shootGuardUpper[key], shootMyselfUpper[key])):
            shootGuardUpper.pop(key)
    check = set(shootMyselfLower) & set(shootGuardLower)
    for key in check:
        if(bigger(shootGuardLower[key], shootMyselfLower[key])):
            shootGuardLower.pop(key)
    return len(set(shootGuardUpper)) + len(set(shootGuardLower))
if __name__ == '__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
