def is_sorted(n):
    a = list(str(n))
    return a == sorted(a)

def has_adjacent(n):
    a = str(n)
    l = []
    start = 0
    previous = a[0]
    i = 1
    has_two = False
    for _next in a[1:]:
        if previous != _next:
            if (i-start) > 1:
                l.append(a[start:i])
                if len(l[-1]) == 2:
                    has_two = True
            start = i
        previous = _next
        i += 1
    if (i-start) > 1:
        l.append(a[start:i])
        if len(l[-1]) == 2:
            has_two = True
        
    return (len(set(i[0] for i in l)) > 0) and has_two
        

def count_passwords(low=402328, high=864247):
    i = low
    count = 0
    l = []
    while i <= high:
        if has_adjacent(i) and is_sorted(i):
            count += 1
            l.append(i)
        i += 1
    return count, l

if __name__ == '__main__':
    print count_passwords()
    # print has_adjacent(112233)
