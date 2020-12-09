import re
import sys


def vm(tape):
    idx = 0
    seen = set()
    accumulator = 0
    while idx not in seen and idx < len(tape):
        seen.add(idx)
        instr, sign, value = tape[idx]
        if instr == 'nop':
            idx += 1
        elif instr == 'acc':
            if sign == '-':
                accumulator -= int(value)
            else:
                accumulator += int(value)
            idx += 1
        elif instr == 'jmp':
            if sign == '-':
                idx -= int(value)
            else:
                idx += int(value)
    return accumulator, idx >= len(tape)

def part1(tape):
    accumulator, condition = vm(tape)
    return accumulator

def part2(tape):
    idx = 0
    while idx < len(tape):
        updated_tape = tape[:]
        if tape[idx][0] == 'jmp':
            updated_tape[idx] = ('nop', tape[idx][1], tape[idx][2])
        elif tape[idx][0] == 'nop':
            updated_tape[idx] = ('jmp', tape[idx][1], tape[idx][2])
        accumulator, condition = vm(updated_tape)
        if condition:
            return accumulator
        idx += 1


if __name__ == '__main__':
    tape = [
        re.findall(r'(\w+) ([+-]+)(\d+)$', line.strip())[0] for line in sys.stdin.readlines()]
    print part1(tape)
    print part2(tape)
