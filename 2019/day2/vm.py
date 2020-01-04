def init(data, noun, verb):
    a = [int(i) for i in data.split(',')]
    a[1] = noun
    a[2] = verb
    return a

def vm(data, noun=12, verb=2):
    tape = init(data, noun, verb)
    pos = 0
    while tape[pos] != 99 and pos < len(tape):
        if tape[pos] == 1:
            tape[tape[pos + 3]] = tape[tape[pos+1]] + tape[tape[pos+2]]
            pos += 4
        elif tape[pos] == 2:
            tape[tape[pos + 3]] = tape[tape[pos+1]] * tape[tape[pos+2]]
            pos += 4
        else:
            assert tape[pos] == 99, tape[pos]
            pos += 1
            break
        
    return tape[0]

def vm2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            value = vm(data, noun, verb)
            if value == 19690720:
                return 100 * noun + verb
    

if __name__ == '__main__':

    # print vm("1,9,10,3,2,3,11,0,99,30,40,50")
    # print vm("1,1,1,4,99,5,6,0,99")
    print vm2("1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0")

    
