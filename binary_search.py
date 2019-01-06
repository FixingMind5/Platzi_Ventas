import random

def binarySearch(data, target, startsAt, endsAt):
    if startsAt > endsAt:
        print("No there isn't")
        return False

    mid = int((startsAt + endsAt) / 2)

    if target == data[mid]:
        print("YES! There is")
        return True
    elif target < data[mid]:
        return binarySearch(data, target, startsAt, mid - 1)
    else:
        return binarySearch(data, target, mid + 1, endsAt)


if __name__ == '__main__':
    """data = [random.randint(0, 100) for i in range(10)]"""
    data = []

    for i in range(10):
        data.append(random.randint(0, 100))

    data.sort()
    print(data)

    target = int(input("Number: "))
    found = binarySearch(data, target, 0, len(data) - 1)
