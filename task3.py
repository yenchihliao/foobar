# Evil empire has a prison. The prisoner's ID is arange as below:
# 11
# 7 12
# 4 8 13
# 2 5 9 14
# 1 3 6 10 15
# The opsition(x, y) denotes the prison in x-th floor and the y-th position
# from the wall. Report the prisoner's ID given their position.

def solution(x, y):
    # Your code here
    tmp = (x+y-2)
    return str((tmp + 1) * tmp / 2 + x)

if __name__ == '__main__':
    print(solution(5, 10))
    print(solution(3, 2))

