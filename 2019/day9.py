import itertools
from vm import VM

def part1():
    # program = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    # program = "1102,34915192,34915192,7,4,7,99,0"
    # program = "104,1125899906842624,99"
    program = open("day9-input.txt").read()
    vm = VM(program, iter([lambda: 1]))
    try:
        while True:
            vm.run()
    except:
        print vm.outputs

if __name__ == '__main__':
    part1()
