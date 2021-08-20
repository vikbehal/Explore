def solve(arr, n):
    for idx, num in enumerate(arr):
        if num == n:
            return n, n
        elif num > n and idx != 0:
            return num, arr[idx - 1]
        elif num > n and idx == 0:
            return num, None

    print("ceil found as {} & floor as {}".format(num, arr[idx - 1]))

    # when nothing is found
    return None, arr[-1]


def solveBST(arr, n):
    print("solving for arr {}".format(arr))
    if n < arr[0]:
        return [arr[0]]
    if n > arr[len(arr)-1]:
        return [-1]

    mid = len(arr) // 2

    if arr[mid] == n:
        return [n]
    elif len(arr) <= 2:
        for val in arr:
            if val == n:
                return [val]
        return arr
    elif n < arr[mid]:
        return solveBST(arr[:mid + 1], n)
    else:
        return solveBST(arr[mid:], n)


arr = [1, 4, 6, 8, 9]
num = 7
#print(solve(arr, num))
print("Using BST")
output = solveBST(arr, num)
if len(output) == 2:
    floor, ceil = output
    print("{},{}".format(floor, ceil))
else:
    print(output[0])
