def maxDistance(arr):
    maxDist = 0
    map = {}
    for idx, item in enumerate(arr):
        if item in map:
            distance = idx - map[item]  # latest index - first index
            maxDist = distance if distance > maxDist else maxDist  # update maximum distance
        else:
            map[item] = idx  # first index

    return maxDist


arr = list(map(int, "3,2,1,2,1,4,5,8,6,7,4,2".split(',')))
print(maxDistance(arr))