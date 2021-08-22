def min_fairness(lst, k):
    lst = sorted(lst)
    #print(lst)
    minimum = []
    n = len(lst)
    for idx in range(n):
        end = idx + k
        if end <= n:
            minimum.append(lst[end - 1] - lst[idx])
        else:
            break

    return min(minimum)


k = int("3")
l = list(map(int, "8,14,20,10,15".split(",")))
print(min_fairness(l, k))