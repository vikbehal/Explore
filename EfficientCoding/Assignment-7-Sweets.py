n = 6
data = ["3 6", "1 6", "7 11", "2 15", "5 8", "1 2"]

votes = {}
#for _ in range(int(input())):
for idx in range(n):
    X, Y = [int(num) for num in data[idx].split(" ")]
    # count positive vote for every minimum sweet and negative vote for maximum+1 sweet.
    # vote +1 for each sweet that is minimum acceptable and -1 for maximum+1
    if X in votes:
        votes[X] += 1
    else:
        votes[X] = 1
    if Y + 1 in votes:
        votes[Y + 1] -= 1
    else:
        votes[Y + 1] = -1

happypeople = 0
nsweets, npeople = 0, 0
# print(sorted(votes.items()))
# sorted will sort based on number of sweets
for sweets, vote in sorted(votes.items()):
    # positive vote increases the happypeople and negative decreases so everytime we see a negative number we are making
    # more kids unhappy. So, for every X (say 10) votes we need at least X (say 10) votes to reach same state. Once that
    # state is reached then another positive vote will help secure a new set of kids which are happy with minimum sweets
    happypeople += vote

    # if previous vote hasn't been able to supress previous best then it is not the best solution so far
    if happypeople > npeople:
        npeople, nsweets = happypeople, sweets
    else:
        # this is the case where negative votes will be ignored
        pass

print("{} {}".format(nsweets, npeople))