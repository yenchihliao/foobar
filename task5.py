" There are 3 operations: +1, -1, /2
" Find the sequence of least operations that turns positive integer into 1
" The number is at most 309 digit
def solution(n):
    n = int(n)
    ret = 0
    layer = 0 # bound = 2^layer > current n
    bound = 1 # bound > current n
    powList = [1] # powList[k] = 2^k
    while(bound <= n):
        bound <<= 1
        layer += 1
        powList.append(bound)
    while(layer > 1):
        # print('in while: ', layer, n)
        # n/2 always has the priority
        if(n % 2 == 0):
            while(n % 2 == 0):
                # print('div')
                n >>= 1
                ret += 1
                layer -= 1
            continue
        # decide to + or - by binary searching within the layer of layer-1
        # deal with edge condition(left and right most) first
        elif(n - 1 == powList[layer-1]):
            # print('left')
            n = powList[layer-1]
            ret += 1
        elif(n + 1 == powList[layer]):
            # print('right')
            n = powList[layer]
            layer += 1
            ret += 1
        else:
            grain = layer - 2 # grain indicates middle positionin binary search
            cut = powList[layer-1] + powList[grain]
            while(grain > 1):
                grain -= 1
                if(n + 1 == cut or n - 1 == cut):
                    n = cut
                    ret += 1
                    break
                elif(n > cut):
                    cut += powList[grain]
                else:
                    cut -= powList[grain]
    return ret
if __name__ ==  '__main__':
    for i in range(1, 18):
        print(i, solution(str(i)))
