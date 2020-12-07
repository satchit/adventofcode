import sys
import re

def part1(text):
    parent_tree = {}
    for line in text.splitlines():
        bags = re.findall(r'\d?([a-z ]+) bag[s]?', line.strip())
        for bag in bags[1:]:
            bag = bag.strip()
            if bag not in parent_tree:
                parent_tree[bag] = set()
            parent_tree[bag].add(bags[0].strip())
    ancestors = []
    done = set()
    l = list(parent_tree['shiny gold'])
    while l:
        bag = l.pop()
        if bag not in done:
            done.add(bag)
            ancestors.append(bag)
            if bag in parent_tree:
                l.extend(parent_tree[bag])
    return len(ancestors)

def generate_child_tree(text):
    child_tree = {}
    for line in text.splitlines():
        bags = re.findall(r'(\d?)\W?([a-z ]+) bag[s]?', line.strip())
        child_tree[bags[0][1]] = bags[1:]
    return child_tree

def part2(data, bag, count):
    if bag not in data:
        return count
    return count + sum(count*part2(data, b[1], int(b[0])) for b in data[bag])

if __name__ == '__main__':
    data = sys.stdin.read()
    print part1(data)
    print part2(generate_child_tree(data), 'shiny gold', 1) - 1 # subtract 1 because we double count the initial bag