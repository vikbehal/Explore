def findMaxSum(input_list):
    previous = input_list[0]
    current = max(input_list[0], input_list[1])

    for val in input_list[2:]:
        val_max = max(current, previous + val)
        print(val_max)
        previous = current
        current = val_max if val_max > val else val

    return current


input_list = "-2,1,3,-4,5"
input_list = input_list.split(",")
input_list = [int(val) for val in input_list]
print(findMaxSum(input_list))
