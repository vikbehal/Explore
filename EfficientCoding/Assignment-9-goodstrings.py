def solve(badstring):
    goodstring =[badstring[i] for i in range(len(badstring)-1) if badstring[i] != badstring[i+1]]
    # add last char as-is
    goodstring += [badstring[-1]]
    return "".join(goodstring)

# for _ in range(int(input())):
#     print(solve(input()))

n = 4
data = ["abb", "aaab", "ababa", "aabbaa"]

for i in range(n):
    print(solve(data[i]))