import collections
import decimal
import math

def calc_m_and_c(p1, p2):
    if p1[0] == p2[0]:
        return (None, p1[0])
    elif p1[1] == p2[1]:
        return (0, p1[1])
    else:
        x1, y1 = p1
        x2, y2 = p2
        m = decimal.Decimal(y2-y1)/(x2 - x1)
        c = y1 - m*x1
        return m.quantize(decimal.Decimal('.0001', decimal.ROUND_UP)), c.quantize(decimal.Decimal('.0001', decimal.ROUND_UP))

def calc_angle_and_radius(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    radius = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    angle = math.atan2(decimal.Decimal(y1-y2), decimal.Decimal(x2-x1))
    b = angle*180/math.pi
    if b < 0:
        b = 360 + b
    c = 360 - b
    d = (c + 90) % 360.0
    return d, radius

def part2(x, grid):
    angle_dict = {}
    points_dict = {}
    for p in grid:
        if p == x:
            continue
        angle, radius = calc_angle_and_radius(x, p)
        if angle not in angle_dict:
            angle_dict[angle] = []
        angle_dict[angle].append((radius, p))
        points_dict[p] = (angle, radius)
    return angle_dict, points_dict
        

if __name__ == '__main__':
    import sys
    grid = []
    with open(sys.argv[1]) as f:
        data = [l.strip() for l in f.readlines()]
        max_y = len(data)
        for yi, y in enumerate(data):
            y = y.strip()
            max_x = len(y)
            for xi, x in enumerate(y):
                if x == '#':
                    grid.append((xi, yi))
        #print grid
    line_dict = {}
    for p1 in grid:
        for p2 in grid:
            if p1 == p2:
                continue
            else:
                t = calc_m_and_c(p1, p2)
                if t not in line_dict:
                    line_dict[t] = set([p1])
                line_dict[t].add(p2)

    for k, v in line_dict.items():
        if (1,0) in v:
            print k, sorted(v)

    print

    sight_counts = collections.Counter()
    for line_points_set in line_dict.values():
        line_points = sorted(line_points_set)
        line_points.sort()
        if (1,0) in line_points:
            print line_points
        # print "counts: ", line_points
        sight_counts[line_points[0]] += 1
        sight_counts[line_points[-1]] += 1
        for p in line_points[1:-1]:
            sight_counts[p] += 2

    # print

    # for y in range(max_y):
    #     l = []
    #     for x in range(max_x):
    #         if (x, y) in grid:
    #             l.append('#')
    #         else:
    #             l.append('.')
    #     print ''.join(l)

    # print
            
    # for y in range(max_y):
    #     l = []
    #     for x in range(max_x):
    #         if (x, y) in sight_counts:
    #             l.append(str(sight_counts[(x,y)]))
    #         else:
    #             l.append('.')
    #     print ''.join(l)
    

    # print

    x, x_count = sight_counts.most_common()[0]

    angle_dict, points_dict = part2(x, grid)

    count = 0
    while count < 200:
        for angle in sorted(angle_dict.keys()):
            if angle_dict[angle]:
                p = angle_dict[angle].pop(0)
                count += 1
                print count
                if count == 200:
                    print p
                    break
    
    # for ya in range(max_y):
    #     l = []
    #     for xa in range(max_x):
    #         if (xa, ya) == x:
    #             l.append("X")
    #         elif (xa, ya) in points_dict:
    #             angle = points_dict[(xa,ya)][0]
    #             l.append(str(decimal.Decimal(angle).quantize(decimal.Decimal('1.1'))))
    #         else:
    #             l.append('.')
    #     print '\t'.join(l)

    # print
    # print

    # for ya in range(max_y):
    #     l = []
    #     for xa in range(max_x):
    #         if (xa, ya) == x:
    #             l.append("X")
    #         elif (xa, ya) in points_dict:
    #             angle = points_dict[(xa,ya)][1]
    #             l.append(str(decimal.Decimal(angle).quantize(decimal.Decimal('1.1'))))
    #         else:
    #             l.append('.')
    #     print '\t'.join(l)
    

            
            
