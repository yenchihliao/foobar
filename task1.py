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
