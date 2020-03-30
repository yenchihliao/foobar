import time
from copy import deepcopy
# C(a, b):
#     nominator = 1
#     for i in range(b+1, a+1):
#         nominator *= i
#     denominator = 1
#     for i in range(1, a-b+1):
#         denominator *= i
#     return nominator / denominator
def show(result):
    for row in result:
        for e in row:
            print e,
        print ""
def tryNext(status):
    count = 0
    done = True
    for i in range(len(status)):
        reverseIndex = len(status) - i - 1
        if(not status[reverseIndex]): # Find 0(s) in status in the reverse order
            count += 1
            if(i == count - 1): # Find the last 0 that can make progress
                status[reverseIndex] = True
                continue
            else: # make some progress
                done = False
                status[reverseIndex] = True
                while(count != 0):
                    reverseIndex += 1
                    count -= 1
                    status[reverseIndex] = False
                break
    return done

def solution(bunny, require):
    # numberRequire = C(bunny, require-1)
    status = [True] * bunny
    for i in range(require - 1):
        status[i] = False
    result = []
    for _ in range(bunny):
        result.append([])
    if(require == 0):
        return result
    done = False
    while(not done):
        for i in range(bunny):
            result[i].append(status[i])
        done = tryNext(status)
    ret = []
    for _ in range(bunny):
        ret.append([])
    for bunnyID in range(bunny):
        count = 0
        while(len(result[bunnyID]) != 0):
            if(result[bunnyID].pop()):
                ret[bunnyID].append(count)
            count += 1
    return ret


if __name__ == '__main__':
    print(solution(5, 3))
    print(solution(3, 1))
    print(solution(2, 1))
    print(solution(2, 0))
    print(solution(5, 5))

