import sys

def parse_input(text):
    return [list(line.strip()) for line in text.splitlines()]

def get_trees(grid, right, down):
    height = len(grid)
    columns = len(grid[0])

    trees = 0

    y = currentx = 0
    while y < len(grid):
        for x in range(right):
            currentx += 1
            if currentx == columns:
                currentx = 0
        y += down
        if y < len(grid) and grid[y][currentx] == '#':
            trees += 1
    return trees

def part1(grid):
    return get_trees(grid, 3, 1)

def part2(grid):
    product = 1
    for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]: 
        product *= get_trees(grid, *slope)
    return product 


if __name__ == '__main__':
    grid = parse_input(sys.stdin.read())
    print part1(grid)
    print part2(grid)