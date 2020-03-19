def solution(x, y):
    # Your code here
    tmp = (x+y-2)
    return str((tmp + 1) * tmp / 2 + x)

if __name__ == '__main__':
    print(solution(5, 10))
    print(solution(3, 2))

