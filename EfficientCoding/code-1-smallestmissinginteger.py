def smallMissingNumber(arr, size):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    print(map)

    index = 1
    while True:
        if index in map:
            index += 1
        else:
            return index


arr = [-5, 2, 0, -1, -10, 15, -5]
size = len(arr)
print("Smallest positive missing number is : ", smallMissingNumber(arr, size))
