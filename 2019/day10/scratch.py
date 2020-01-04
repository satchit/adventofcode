import math

print "x, y: val"
for y in range(-1, 2):
    for x in range(-1, 2):
        a = math.atan2(y,x)
        b = a*180/3.14
        if b < 0:
            b = 360 + b
        c = 360 - b
        d = (c + 90) % 360
        print x, ", ", y, ": ",  b, c, d
