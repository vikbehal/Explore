class PurchaseTime:
    def __init__(self):
        self.debug = True

    def totalpurchasetime(self, tickets, pos):
        total_time = tickets[pos]
        for idx, ticket in enumerate(tickets):
            if idx < pos:
                if tickets[idx] < tickets[pos]:
                    total_time += tickets[idx]
                else:
                    total_time += tickets[pos]
            elif idx > pos:
                if tickets[idx] < tickets[pos]:
                    total_time += tickets[idx]
                else:
                    total_time += tickets[pos] - 1

        return total_time

print("*********Specific case*********")
p = PurchaseTime()
tickets = [2, 6, 3, 4, 5]
pos = 2
total_time = p.totalpurchasetime(tickets, pos)
print("total time: {} for position {}".format(total_time, pos))

print("*********Use-case1*********")

# All positions
tickets = [2, 6, 3, 4, 5]
all_time = list(map(lambda x: p.totalpurchasetime(tickets, x), range(len(tickets))))
for pos, time in zip(range(len(tickets)), all_time):
    print("Jesse would take '{}' time if started at position '{}'".format(time, pos))

print("*********Use-case2*********")

tickets = [5, 5, 2, 3]
all_time = list(map(lambda x: p.totalpurchasetime(tickets, x), range(len(tickets))))
for pos, time in zip(range(len(tickets)), all_time):
    print("Jesse would take '{}' time if started at position '{}'".format(time, pos))
