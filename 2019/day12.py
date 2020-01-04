from __future__ import print_function
import itertools


class Moon(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def position(self):
        return self.x, self.y, self.z

    def velocity(self):
        return self.vx, self.vy, self.vz

    def apply_velocity(self, vx, vy, vz):
        self.x += vx
        self.y += vy
        self.z += vz
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def energy(self):
        return sum(abs(i) for i in self.position()) * sum(abs(i) for i in self.velocity())
        
    def __str__(self):
        return "pos=<x= %d, y= %d, z= %d>, vel=<x= %d, y= %d, z= %d>" % (
            self.x, self.y, self.z, self.vx, self.vy, self.vz)

def construct_moon(data):
    return Moon(*[int(i.split('=')[-1]) for i in data.strip().strip('>').strip('<').split(',')])
    
def velocity_delta(m1, m2):
    delta = [-cmp(*axis) for axis in zip(m1.position(), m2.position())]
    return delta, [-i for i in delta]

def advance_by_time_unit(moons):
    new_velocity = dict((m, m.velocity()) for m in moons)
    for m1, m2 in itertools.combinations(moons, 2):
        m1_delta, m2_delta = velocity_delta(m1, m2)
        new_velocity[m1] = map(sum, zip(new_velocity[m1], m1_delta))
        new_velocity[m2] = map(sum, zip(new_velocity[m2], m2_delta))
    for m in moons:
        m.apply_velocity(*new_velocity[m])



def part1(moons):
    map(print, moons)
    print("")
    print("")
    steps = 1000
    for i in range(1, steps+1):
        advance_by_time_unit(moons)
        print("After %d steps:" % i)
        map(print, moons)
        print("")
        print("")
    return sum(m.energy() for m in moons)


def part2(moons):
    configs = set(tuple(((m.position(), m.velocity()) for m in moons)))
    count = 0
    while True:
        advance_by_time_unit(moons)
        count += 1
        config = tuple(((m.position(), m.velocity()) for m in moons))
        print(config)
        if config in configs:
            break
        configs.add(config)
        if count % 100 == 0:
            print(count)
    map(print, moons)
    print("repeats after %d counts" % count)
    print(config)


if __name__ == '__main__':
    test1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

    test2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

    day12_input = """<x=-7, y=-8, z=9>
<x=-12, y=-3, z=-4>
<x=6, y=-17, z=-9>
<x=4, y=-10, z=-6>"""

    moons = [construct_moon(l.strip()) for l in test1.splitlines()]
    part2(moons)
        
