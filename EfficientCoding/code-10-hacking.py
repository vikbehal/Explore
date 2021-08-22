def getCount(N, K, given_state):
    m = {
        "R": 0,
        "Y": 1,
        "G": 2
    }

    for state in given_state:
        if state == "R":

    print(m)


N, K = (int(x) for x in "4 2".split())
m = {'G': 0, 'R': 1, 'Y': 2}
given_state = [m[x] for x in "R Y G Y".split()]

print(getCount(N, K, given_state))