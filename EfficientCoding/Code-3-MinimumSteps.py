def solve(start, goal):
    steps = 0
    multiply = 2
    add = 1

    # reduce to minimum by division
    while True:
        if goal % multiply == 0:
            goal = int(goal / multiply)
        elif (goal-add) % multiply == 0:
            goal -= add
        else:
            start += add

        steps += 1

        print("start {} goal {}".format(start, goal))

        if start == goal:
            break

    return steps


start, goal = 0, 6
print("total steps {}".format(solve(start, goal)))
