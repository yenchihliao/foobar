# Evil empire has a system, the version number of it includes a main version, subversion, and a fix number
# Version number begins from 1. However, beta versions has a version number of 0
# subversion number and fix number is optional. Sort the version numbers to please your evil boss
def isfront(a, b):
    A = a.split('.')
    B = b.split('.')
    i = 0
    while(True):
        if int(A[i]) > int(B[i]) :
            return False
        elif int(A[i]) < int(B[i]):
            return True
        else:
            i += 1
            if len(A) == i:
                return True
            elif len(B) == i:
                return False
    return False
def solution(l):
    length = len(l)
    if(length == 1):
        return l
    left = solution(l[:len(l)//2])
    right = solution(l[len(l)//2:])
    iLeft = 0
    iRight = 0
    newL = []
    while(True):
        if(isfront(left[iLeft], right[iRight])):
            newL.append(left[iLeft])
            iLeft += 1
        else:
            newL.append(right[iRight])
            iRight += 1
        if(iLeft == len(left)):
            for v in right[iRight:] :
                newL.append(v)
            break
        elif(iRight == len(right)):
            for v in left[iLeft:] :
                newL.append(v)
            break
    return newL
# iLeft != len(left) and iRight != len(right)
if __name__ == '__main__':
    l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
    print(solution(l))
