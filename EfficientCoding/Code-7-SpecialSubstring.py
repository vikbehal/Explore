def get_special_count(s):
    l = []
    current = None
    count = 0

    # Find running count of same characters
    for idx, c in enumerate(s):
        # print("procesing {} current {} count {}".format(c, current, count))
        if c == current:
            count += 1
        else:
            if current is not None:
                l.append((current, count))

            current = c
            count = 1

    l.append((current, count))

    answer = 0

    # Case 1: Count possible characters
    for charSet in l:
        n = charSet[1]
        answer += (n * (n + 1)) // 2

    # Case 2 Count by ignoring middle char
    for idx in range(1, len(l) - 1):
        if l[idx - 1][0] == l[idx + 1][0] and l[idx][1] == 1:
            minimumAns = min(l[idx - 1][1], l[idx + 1][1])
            answer += minimumAns

    return answer


s = "mnonopoO"
print(get_special_count(s))
