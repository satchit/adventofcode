import sys

WIDTH = 25
HEIGHT = 6

def decode_pixel(l):
    for i in l:
        if i == '0':
            return ' ' # to make characters readable
        elif i == '1':
            return i
    return '2'

if __name__ == '__main__':
    data = [i for i in list(open('input.txt').read().strip())]
    layer_size = WIDTH*HEIGHT
    layers = [data[idx:idx+layer_size] for idx in range(len(data))[::layer_size]]
    image = [decode_pixel(l) for l in zip(*layers)]
    print '\n'.join([''.join(image[idx:idx+WIDTH]) for idx in range(len(image))[::WIDTH]])


            
