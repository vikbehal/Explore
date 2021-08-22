def solve(seq):
    answers = []
    for s1 in seq:
        k, s = s1.split(" ")
        k = int(k)
        if k == 1:
            res = s

            for i in range(1, len(s)):
                left = s[i:]
                right = s[:i]
                rotated_string = left+right

                if rotated_string < res:
                    res = rotated_string

            answers.append(res)
        else:
            res = "".join(sorted(s))
            answers.append(res)

    return answers


# for input use:
# n = int(input())
# seq = []
# for i in range(n):
#     s = input()
#     seq.append(s)
# answers = solve(seq)
# for ans in answers:
#     print(ans)


n = int(2)
seq = ["1 cba", "2 abab"]
answers = solve(seq)
for ans in answers:
    print(ans)
