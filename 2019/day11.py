import itertools
from vm import VM

#N,W,S,E = (0,1,2,3)
#L,R = (0,1)

next_step = {
    #curr_dir, dir -> (new_loc, new_dir)
    #N, L
    (0, 0): lambda x, y: ((x-1, y), 1),
    (0, 1): lambda x, y: ((x+1, y), 3),
    (1, 0): lambda x, y: ((x, y-1), 2),
    (1, 1): lambda x, y: ((x, y+1), 0),
    (2, 0): lambda x, y: ((x+1, y), 3),
    (2, 1): lambda x, y: ((x-1, y), 1),
    (3, 0): lambda x, y: ((x, y+1), 0),
    (3, 1): lambda x, y: ((x, y-1), 2),
    }

def part1():
    program = open("day11-input.txt").read()
    vm = VM(program, iter([lambda: 0]))
    grid = {(0, 0): 1}
    curr_loc = (0, 0)
    curr_dir = 0
    count = 0
    try:
        while True:
            vm.run()
            color = vm.get_output()
            print "color: ", color
            vm.run()
            dir = vm.get_output()
            print "dir: ", dir
            grid[curr_loc] = color
            curr_loc, curr_dir = next_step[(curr_dir, dir)](*curr_loc)
            if curr_loc not in grid:
                grid[curr_loc] = 0
            vm.append_inputs(iter([lambda: grid[curr_loc]]))
    except:
        print grid
        print len(grid)

    max_x = max(i[0] for i in grid.keys())
    min_x = min(i[0] for i in grid.keys())
    max_y = max(i[1] for i in grid.keys())
    min_y = min(i[1] for i in grid.keys())

    grid2d = [[' ' for x in range(min_x, max_x+100)] for y in range(min_y, max_y+100)]
    mid_y = len(grid2d)/2
    mid_x = len(grid2d[0])/2
    print len(grid2d[0]), mid_x, len(grid2d), mid_y
    for key, color in grid.items():
        # print key
        if color == 1:
            grid2d[mid_y+key[1]][mid_x+key[0]] = '1'
    for row in grid2d:
        print ''.join(row)
    
def part2():
    program = open("day11-input.txt").read()
    vm = VM(program, iter([lambda: 1]))
    grid = {(0, 0): 1}
    curr_loc = (0, 0)
    curr_dir = 0
    count = 0
    try:
        while True:
            vm.run()
            color = vm.get_output()
            print "color: ", color
            vm.run()
            dir = vm.get_output()
            print "dir: ", dir
            grid[curr_loc] = color
            curr_loc, curr_dir = next_step[(curr_dir, dir)](*curr_loc)
            if curr_loc not in grid:
                grid[curr_loc] = 0
            vm.append_inputs(iter([lambda: grid[curr_loc]]))
    except:
        print grid
        print len(grid)

    max_x = max(i[0] for i in grid.keys())
    min_x = min(i[0] for i in grid.keys())
    max_y = max(i[1] for i in grid.keys())
    min_y = min(i[1] for i in grid.keys())

    mid_x = (min_x + max_x)/2
    mid_y = (min_y + max_y)/2

    grid2d = [[' ' for x in range(min_x-mid_x, max_x+mid_x)] for y in range(min_y-mid_y-1, max_y+mid_y+10)]
    mid_y = len(grid2d)/2
    mid_x = len(grid2d[0])/2
    print min_x, mid_x, max_x, min_y, mid_y, max_y
    for key, color in grid.items():
        if color == 1:
            grid2d[mid_y+key[1]][mid_x+key[0]] = '#'
    for row in grid2d:
        print ''.join(row)

if __name__ == '__main__':
    part2()
