" Problem about absorbing markov chain

from fractions import Fraction
from fractions import gcd

def show(m):
    for row in m:
        for e in row:
            print e,
        print ""
    print("-------")

def lcm(a, b):
    return a * b / gcd(a, b)

def minus2Row(m, a, b, n): # minus n * a to row b
    if(a == b):
        return
    for i in range(len(m)):
        m[b][i] -= m[a][i] * n
def mul(m, a, n): # multiply row a by n in matrix m
    if(n == 1):
        return
    for i in range(len(m)):
        m[a][i] *= n
def changeRow(m, a, b): # exchange row a and b of matrix m
    if(a == b):
        return
    m[a], m[b] = m[b], m[a]

def NbyQ(Q):
    # tmp = I-Q
    tmp = []
    for i in range(len(Q)):
        tmp.append([])
        for j in range(len(Q)):
            if(i != j):
                tmp[i].append(-1 * Q[i][j])
            else:
                tmp[i].append(1 - Q[i][j])
    ## inverse by Gussian
    N = []
    for i in range(len(tmp)):
        N.append([Fraction(0)] * len(tmp))
    for i in range(len(tmp)):
        N[i][i] = 1
    ### find the first row in every colume that has value aside from 1
    for col in range(len(tmp)):
        found = False
        row  = col
        while(row < len(tmp)):
            if(tmp[row][col] != 0):
                found = True
                # print("found ", row)
                break
            row += 1
        if(found):
            ### multiply to become 1
            mul(N, row, Fraction(1, tmp[row][col]))
            mul(tmp, row, Fraction(1, tmp[row][col]))
            ### clean other elements in the same colume
            for i in range(len(tmp)):
                minus2Row(N, row, i, tmp[i][col])
                minus2Row(tmp, row, i, tmp[i][col])
            ### swap to the correct position
            changeRow(N, row, col)
            changeRow(tmp, row, col)
    return N
def solution(m):
    absorbIndex = []
    absorbCount = 0
    for i, row in enumerate(m):
        denominator = sum(row)
        if(denominator):
            absorbIndex.append(False)
        else:
            absorbIndex.append(True)
            absorbCount += 1
    if absorbCount <= 1:
        return [1, 1]
    Q = []
    R = []
    for i in range(len(m)):
        if(absorbIndex[i]):
            continue
        denominator = sum(m[i])
        qRow = []
        rRow = []
        for j in range(len(m)):
            if(absorbIndex[j]):
                rRow.append(Fraction(m[i][j], denominator))
            else:
                qRow.append(Fraction(m[i][j], denominator))
        Q.append(qRow)
        R.append(rRow)
    N = NbyQ(Q)
    result = [Fraction(0)] * absorbCount
    for i in range(len(N)):
        for j in range(absorbCount):
            result[j] += N[0][i] * R[i][j]
    # print(result)
    denominator = result[0].denominator
    for i in range(1, absorbCount):
       denominator = lcm(denominator, result[i].denominator)
    # print(denominator)
    for i in range(absorbCount):
        result[i] = int(result[i] * denominator)
    result.append(denominator)
    if len(N) == 0:
        result[0] = 1
    return result

if __name__ == '__main__':
    m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    print(solution(m))
    m =  [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    print(solution(m))
    m = [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(solution(m))
