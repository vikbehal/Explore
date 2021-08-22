def solve(N, K, str):
    out = ""
    m = {}

    for c in str:
        if c not in m:
            m[c] = 1
            out += c
        else:
            if m[c] < K:
                m[c] += 1
                out += c

        # max check
        # print(len(out))
        if len(out) == 26 * K:
            break

    return out


feed = ["ababbca", "abcaacbccb"]
nums = ["8 2", "10 3"]
for idx in range(int(2)):
    N, K = [int(num) for num in nums[idx].split(" ")]
    str = feed[idx]
    print(solve(N, K, str))

# for _ in range(int(input())):
#     N, K = [int(num) for num in input().split(" ")]
#     str = input()
#     print(solve(N, K, str))
