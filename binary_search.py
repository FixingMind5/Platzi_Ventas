import random

def binarySearch(d, t, s, e):
    x = False
    m = 0

    if s > e:
        x = False

    while s <= e:
        m = (s + e) // 2

        if t == d[m]:
            x = True
            return m
            break
        elif t < d[m]:
            e = m - 1
        else:
            s = m + 1

    return x



if __name__ == '__main__':
    """data = [random.randint(0, 100) for i in range(10)]"""
    d = []

    for i in range(10):
        d.append(random.randint(0, 100))

    d.sort()
    print(d)

    t = int(input("Number: "))
    found = binarySearch(d, t, 0, len(d) - 1)
    print("{} number is at {} position".format(t, found))
