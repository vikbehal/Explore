def solve(inputList):
    # Edge cases
    if sum(inputList[1:]) == 0:
        return 0
    totalItems = len(inputList)
    if sum(inputList[:totalItems - 1]) == 0:
        return totalItems - 1

    leftSum = 0
    rightSum = sum(inputList)

    for idx, item in enumerate(inputList):
        rightSum -= item

        if leftSum == rightSum:
            return idx

        leftSum += item

    return -1


#inputString = input()
inputString = "3,-4, 2, -1,-3, 2, 1"
inputList = [int(val) for val in inputString.split(",")]
print(solve(inputList))