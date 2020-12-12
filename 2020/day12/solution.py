import sys

def rotate(state, direction, delta):
    if direction == 'L':
        if delta == 90:
            state = (-state[1], state[0])
        elif delta == 180:
            state = (-state[0], -state[1])
        elif delta == 270:
            state = (state[1], -state[0])
    elif direction == 'R':
        if delta == 90:
            state = (state[1], -state[0])
        elif delta == 180:
            state = (-state[0], -state[1])
        elif delta == 270:
            state = (-state[1], state[0])
    return state

def part1(data):
    location = (0, 0)
    state = (1, 0)
    for line in data:
        direction, delta = line[0], int(line[1:])
        if direction == 'N':
            location = (location[0], location[1] + delta)
        elif direction == 'S':
            location = (location[0], location[1] - delta)
        elif direction == 'E':
            location = (location[0] + delta, location[1])
        elif direction == 'W':
            location = (location[0] - delta, location[1])
        elif direction == 'F':
            location = (location[0] + state[0] * delta, location[1] + state[1] * delta)
        else:
            state = rotate(state, direction, delta)
    return abs(location[0]) + abs(location[1])

def part2(data):
    waypoint = (10, 1)
    location = (0, 0)
    for line in data:
        direction, delta = line[0], int(line[1:])
        if direction == 'N':
            waypoint = (waypoint[0], waypoint[1] + delta)
        elif direction == 'S':
            waypoint = (waypoint[0], waypoint[1] - delta)
        elif direction == 'E':
            waypoint = (waypoint[0] + delta, waypoint[1])
        elif direction == 'W':
            waypoint = (waypoint[0] - delta, waypoint[1])
        elif direction == 'F':
            location = (location[0] + waypoint[0] * delta, location[1] + waypoint[1] * delta)
        else:
            waypoint = rotate(waypoint, direction, delta)
    return abs(location[0]) + abs(location[1])


if __name__ == '__main__':
    data = [line.strip() for line in sys.stdin.readlines()]
    print part1(data)
    print part2(data)