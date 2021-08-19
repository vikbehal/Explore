def findMaxSum(input_list):
    if len(input_list) == 0:
        return None
    elif len(input_list) == 1:
        return input_list[0]
    else:
        previous = input_list[0]
        current = input_list[1]

        for val in input_list[2:]:
            val_max = val + previous
            previous = current
            current = val_max if val_max > val else val

        return current if current > previous else previous

input_list = "-2,1,3,-4,5"
input_list = input_list.split(",")
input_list = [int(val) for val in input_list]
print(findMaxSum(input_list))