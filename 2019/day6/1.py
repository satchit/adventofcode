import sys

links = {}

class Node():
    label = 0

    def __init__(self, label):
        self.label = label
        self.children = []

    def set_orbit(self, node):
        self.children.append(node)

def get_length(node, i):
    if len(node.children) == 0:
        return i
    else:
        return i + sum(get_length(c, i+1) for c in node.children)

if __name__ == '__main__':
    orbits = [l.strip().split(')') for l in open(sys.argv[1]).readlines()]
    for a, b in orbits:
        if a not in links:
            links[a] = Node(a)
        nodea = links[a]
        if b not in links:
            links[b] = Node(b)
        nodeb = links[b]
        nodea.set_orbit(nodeb)
    print get_length(links['COM'], 0)

        
