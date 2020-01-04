import sys

WIDTH = 25
HEIGHT = 6

if __name__ == '__main__':
    data = [int(i) for i in list(open('input-1.txt').read().strip())]
    layer_size = WIDTH*HEIGHT
    zero_cts = []
    idx = 0
    while idx <= len(data):
        layer = data[idx:idx+layer_size]
        if len(layer) > 0:
            zero_cts.append((layer.count(0), (idx, idx+layer_size)))
        idx = idx+layer_size
    zero_cts.sort()
    print zero_cts
    start, end = zero_cts[0][1]
    layer = data[start:end]
    print layer.count(1)*layer.count(2)


            
