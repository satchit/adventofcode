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

def construct_moon(data):
    return Moon(*[int(i.split('=')[-1]) for i in data.strip().strip('>').strip('<').split(',')])
    
def construct_moons(data):
    return [construct_moon(l.strip()) for l in data.strip().splitlines()]



TEST_CASE_1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

TEST_CASE_2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

DAY12_INPUT = """
<x=-7, y=-8, z=9>
<x=-12, y=-3, z=-4>
<x=6, y=-17, z=-9>
<x=4, y=-10, z=-6>"""

def part1(moons, steps):
    """ Returns total energy after x steps

    >>> moons = construct_moons(TEST_CASE_1)
    >>> part1(moons, 10)
    179

    >>> part1(construct_moons(TEST_CASE_2), 100)
    1940

    >>> part1(construct_moons(DAY12_INPUT), 1000)
    12773
    """
    for i in range(steps):
        advance_by_time_unit(moons)
    return sum(m.energy() for m in moons)

def get_primes(n):
    """ Get list of primes until n/2

    >>> get_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    primes = range(2, n)
    next = 0
    while next < len(primes):
        for idx in range(next+1, len(primes)):
            if idx < len(primes):
                if primes[idx] % primes[next] == 0:
                    primes.pop(idx)
        next += 1
    return primes
        
    
def prime_factors(n, primes):
    """ Given a list of primes returns the prime factors
    >>> prime_factors(10, [2, 3, 5, 7])
    {2: 1, 5: 1}

    >>> prime_factors(16, [2, 3])
    {2: 4}
    """
    factors = []
    i = n
    while i > 1:
        for p in primes:
            if i % p == 0:
                factors.append(p)
                i = i / p
                break
    return dict((p, factors.count(p)) for p in set(factors))
        

def lcm(*args):
    """ lcm(2, 3)
    6

    >>> lcm(2, 6, 15)
    30
    """
    primes = get_primes(max(args))
    factorization = {}
    for n in args:
        factorization[n] = prime_factors(n, primes)
    a = {}
    for factors in factorization.values():
        for p in factors:
            if p not in a:
                a[p] = []
            a[p].append(factors[p])

    value = 1
    for k, v in a.items():
        value *= k**max(v)
    return value
        
    
    
    
def part2(moons):
    """ Returns the steps after which the original config repeats.

    >>> part2(construct_moons(TEST_CASE_1))
    2772

    >>> part2(construct_moons(TEST_CASE_2))
    4686774924

    >>> part2(construct_moons(DAY12_INPUT))
    306798770391636
    """
    configs = set(tuple(((m.position(), m.velocity()) for m in moons)))
    count = 0
    sequences = [[],[],[]]
    repeats_after = {0: None, 1: None, 2: None}
    while True:
        advance_by_time_unit(moons)
        count += 1
        p_and_v = [zip(m.position(), m.velocity()) for m in moons]
        p_and_v_and_m = zip(*p_and_v)
        sequence_by_axis = [tuple(sum([list(j) for j in i], [])) for i in p_and_v_and_m]
        # print(sequence_by_axis)
        for idx, axis in enumerate(sequence_by_axis):
            if axis in sequences[idx] and repeats_after[idx] is None:
                repeats_after[idx] = count - 1
            if not sequences[idx]:
                sequences[idx].append(axis)
        if not filter(lambda x: x is None, repeats_after.values()):
            break
    return lcm(*repeats_after.values())
 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
