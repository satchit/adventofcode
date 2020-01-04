import itertools
from vm import VM

def part1():
    program = open('day7-input.txt').read()
    max_output = None
    for p in itertools.permutations(range(0,5)):
        amp1 = VM(program,itertools.cycle([lambda: p[0], lambda: 0])).run()
        amp2 = VM(program,itertools.cycle([lambda: p[1], amp1.get_output])).run()
        amp3 = VM(program,itertools.cycle([lambda: p[2], amp2.get_output])).run()
        amp4 = VM(program,itertools.cycle([lambda: p[3], amp3.get_output])).run()
        amp5 = VM(program,itertools.cycle([lambda: p[4], amp4.get_output])).run()
        output = amp5.get_output()
        if max_output is None or output > max_output:
            max_output = output
    return max_output

def part2():
    program = open('day7-input.txt').read()
    # program = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    # program = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    max_output = None
    for p in itertools.permutations(range(5, 10)):
        amp1 = VM(program, itertools.chain([lambda: p[0], lambda: 0]), "vm1")
        amp2 = VM(
            program,
            itertools.chain([lambda: p[1]], itertools.cycle([amp1.get_output])),
            "vm2")
        amp3 = VM(
            program,
            itertools.chain([lambda: p[2]], itertools.cycle([amp2.get_output])),
            "vm3")
        amp4 = VM(
            program,
            itertools.chain([lambda: p[3]], itertools.cycle([amp3.get_output])),
            "vm4"
            )
        amp5 = VM(
            program,
            itertools.chain([lambda: p[4]], itertools.cycle([amp4.get_output])),
            "vm5")
        last_output = None
        while True:
            amp1.run()
            amp2.run()
            amp3.run()
            amp4.run()
            amp5.run()
            amp1.append_inputs(itertools.cycle([amp5.get_output]))
            output = amp5.get_output()
            print output
            if output == last_output:
                break
            last_output = output
            if max_output is None or output > max_output:
                max_output = output
            
    return max_output

if __name__ == '__main__':
    print part2()
        
        
    
