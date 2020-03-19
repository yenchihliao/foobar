# Decrypt poorly encrypted sentences to proof that your coworkers are talking about soap opera during work time.
# Since they are not cryptography experts, they simply map a to z, b to y, etc..
def solution(x):
    # Your code here
    ret = ""
    for w in x:
        if 96 < ord(w) < 123:
            ret += chr(219-ord(w))
        else:
            ret += w
    return ret
if __name__ == '__main__':
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
