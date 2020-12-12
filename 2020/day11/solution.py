import math
import re
import sys
import itertools

def get_state_part1(grid, row, col):
    if grid[row][col] == '.':
        return '.'

    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i >= 0 and row + i < rows:
                if col + j >= 0 and col + j < cols:
                    if grid[row + i][col + j] == '#':
                        count += 1
                        if grid[row][col] == '#' and count >= 4:
                            return 'L'
    if grid[row][col] == 'L' and count == 0:
        return '#'    
    return grid[row][col]

def get_state_part2(grid, row, col):
    if grid[row][col] == '.':
        return '.'
    
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    seen = set()
    for deltax in (-1, 0, 1):
        for deltay in (-1, 0, 1):
            for radius in range(10):
                (x, y) = row + deltax * radius, col + deltay * radius
                if (x, y) == (row, col) or (x, y) in seen:
                    continue
                if x >= 0 and x < rows:
                    if y >= 0 and y < cols:
                        seen.add((x, y))
                        if grid[x][y] == '.':
                            continue
                        if grid[x][y] == '#':
                            count += 1
                            if grid[row][col] == '#' and count >= 5:
                                return 'L'
                        break
    if grid[row][col] == 'L' and count == 0:
        return '#'
    return grid[row][col]


def part1(grid):
    while True:
        changed = False
        occupied = 0
        next_grid = []
        for row in range(len(grid)):
            new_row = []
            for col in range(len(grid[0])):
                new_row.append(get_state_part1(grid, row, col))
                if new_row[-1] == '#':
                    occupied += 1
                if grid[row][col] != new_row[-1]:
                    changed = True
            next_grid.append(new_row)
        grid = next_grid
        if not changed:
            break
    return occupied
    

def part2(grid):
    while True:
        changed = False
        occupied = 0
        next_grid = []
        for row in range(len(grid)):
            new_row = []
            for col in range(len(grid[0])):
                new_row.append(get_state_part2(grid, row, col))
                if new_row[-1] == '#':
                    occupied += 1
                if grid[row][col] != new_row[-1]:
                    changed = True
            next_grid.append(new_row)
        grid = next_grid
        if not changed:
            break
    return occupied


def print_grid(grid):
    print '\n'.join(''.join(row) for row in grid)
    print
        
if __name__ == '__main__':
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    print part1(grid)
    print part2(grid)
