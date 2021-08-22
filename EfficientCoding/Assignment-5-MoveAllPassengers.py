def solve(n, cost):
    # print("cost {}".format(cost))
    total_cost = 0
    cost = sorted(cost)
    N = n
    # Move most all except last 3 costly passengers
    # from 3 until end, in reverse since we start moving costly passesnegers first
    for i in range(n - 1, 2, -2):
        # print("n is {}".format(n))
        # move each of the passenger with cheapest passesnger i.e. cost[0]
        cost_choice1 = cost[i] + cost[0] + cost[i - 1] + cost[0]
        # move first two chpeaest passengers first, bring back cheapest one, and then move both costly passengers
        cost_choice2 = cost[1] + cost[0] + cost[i] + cost[1]

        # choose cheapest option
        total_cost += min(cost_choice1, cost_choice2)
        N -= 2

    # print("processing last 3")
    # print(N)
    # print(cost)
    # when last 3 passesngers are left
    if N == 3:
        # the cost will be sum of all. Why? cost of 3 as 1,3 move + cost of 1 to move back + cost of 2 as 1,2 move
        total_cost += sum(cost[:3])
    elif N == 2:
        # the cost of 2nd passenger as 1,2 move
        total_cost += cost[1]
    # elif N == 1:
    # last passenger. Will it even happen?
    # total_cost += cost[0]

    return total_cost

N = 3
Ns = [4,2,3]
data = ["300 400 600 700", "1321 2450", "500 123 873"]

for idx in range(N):
    N = Ns[idx]
    cost = [int(num) for num in data[idx].split(" ")]
    print("processing {}".format(cost))
    min_cost = solve(N, cost)
    print(min_cost)