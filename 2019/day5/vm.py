

def init(data, noun, verb):
    a = [int(i) for i in data.split(',')]
    a[1] = noun
    a[2] = verb
    return a


class VM(object):
    opcode_to_param_count = {
        99: 0,
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3
    }

    def __init__(self, tape):
        self.tape = map(int, tape.strip().split(','))
        
    def parse_operation_and_mode(self, i):
        i = str(i)
        mode, opcode = i[:-2], int(i[-2:])
        try:
            mode = '0' * (self.opcode_to_param_count[opcode] - len(mode)) + mode
        except KeyError:
            print i, opcode, mode[::-1]
        return opcode, mode[::-1]

    def get(self, mode, param):
        if mode == '0':
            return int(self.tape[param])
        else:
            return int(param)

    def _input(self):
        return input()

    def _output(self, val):
        print val
    
    def run(self):
        tape = self.tape
        pos = 0
        while tape[pos] != 99 and pos < len(tape):
            opcode, mode = self.parse_operation_and_mode(tape[pos])
            param_count = self.opcode_to_param_count[opcode]
            args = zip(mode, tape[pos+1:pos+1+param_count])
            if opcode == 1:
                # add
                tape[tape[pos + param_count]] = self.get(*args[0]) + self.get(*args[1])
            elif opcode == 2:
                # multiply
                tape[tape[pos + param_count]] = self.get(*args[0]) * self.get(*args[1])
            elif opcode == 3:
                # get input
                tape[tape[pos + param_count]] = self._input()
            elif opcode == 4:
                # output
                self._output(self.get(*args[0]))
            elif opcode == 5:
                # jump if true
                if self.get(*args[0]) != 0:
                    pos = self.get(*args[1])
                    continue
            elif opcode == 6:
                # jump if false
                if self.get(*args[0]) == 0:
                    pos = self.get(*args[1])
                    continue
            elif opcode == 7:
                # less than
                if self.get(*args[0]) < self.get(*args[1]):
                    val = 1
                else:
                    val = 0
                tape[tape[pos + param_count]] = val
            elif opcode == 8:
                # equals
                if self.get(*args[0]) == self.get(*args[1]):
                    val = 1
                else:
                    val = 0
                tape[tape[pos + param_count]] = val
            else:
                # halt
                assert opcode == 99, tape[pos]
                break
            pos += param_count + 1


if __name__ == '__main__':
    import sys
    # print vm("1,9,10,3,2,3,11,0,99,30,40,50")
    # print vm("1,1,1,4,99,5,6,0,99")
    # vm = VM("1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0")
    vm = VM(open('input.txt').read())
    # vm = VM("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
    # vm = VM("3,3,1105,-1,9,1101,0,0,12,4,12,99,1");
    # vm = VM("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    vm.run()


    
