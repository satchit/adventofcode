import sys

links = {}

class Node():
    label = 0
    parent = None

    def __init__(self, label):
        self.label = label
        self.children = []

    def set_parent(self, node):
        self.parent = node
        
    def set_orbit(self, node):
        self.children.append(node)
        node.set_parent(self)

    def is_descendant(self, node):
        if self == node:
            return [Node]
        else:
            return [c for c in self.children if c.is_descendant(node)]
        
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
    root = links['COM']
    you = node = links['YOU']
    seen = [you]
    while node:
        print node.label, '->',
        node = node.parent
        seen.append(node)

    print
    print

    common = []
    san = node = links['SAN']
    san_parents = [san]
    while node:
        print node.label, '->',
        if node in seen:
            common.append(node)
        node = node.parent
        san_parents.append(node)

    print
    print
    
    print [c.label for c in common]

    print seen.index(common[0]) + san_parents.index(common[0]) - 2 # we don't want the index of you and san.

        
