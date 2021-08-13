def lonelyInteger(a):
    if len(a) == 1:
        return a[0]

    intDict = {}
    for int in a:
        if int in intDict:
            intDict[int] += 1
        else:
            intDict[int] = 1

    print(intDict)
    return list(filter(lambda x: intDict[x] == 1, intDict))


a = [5, 2, 0, 0, 1, 2, 1]
print(lonelyInteger(a))


def lonelyInteger2(a):
    return list(filter(lambda x: a.count(x) == 1, a))

a = [5, 2, 0, 0, 1, 2, 1]
print(lonelyInteger2(a))

def lonelyIntegerXOR(a):
    curr = a[0]
    for i in range(1, len(a)):
        curr ^= a[i]
        print(curr)
    return curr

a = [5, 2, 0, 0, 1, 2, 1]
print(lonelyIntegerXOR(a))