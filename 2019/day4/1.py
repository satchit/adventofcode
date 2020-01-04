def is_sorted(n):
    a = list(str(n))
    return a == sorted(a)

def has_adjacent(n):
    a = str(n)
    previous = a[0]
    for _next in a[1:]:
        if previous == next:
            return True
        else:
            previous = next
    return False

def count_passwords(low=402328, high=864247):
    i = low + 1
    count = 0
    l = []
    while i < high:
        if has_adjacent(i) and is_sorted(i):
            count += 1
            l.append(i)
        i += 1
    return count, len(l), len(set(l))

if __name__ == '__main__':
    print count_passwords()
