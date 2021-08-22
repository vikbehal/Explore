def dfs(row, col, field):
    # print('exploring node {} {}'.format(row, col))
    # Visited
    field[row][col] = 'V'

    rowActions = [0, -1, 0, 1]
    colActions = [-1, 0, 1, 0]

    count = 1
    for r, c in zip(rowActions, colActions):
        newrow = row + r
        newcol = col + c
        # print("checking node {} {} for {} {}".format(newrow, newcol, row, col))
        if newrow >= 0 and newrow < len(field) and newcol >= 0 and newcol < len(field[row]) and field[newrow][
            newcol] == "T":
            count += dfs(newrow, newcol, field)

    return count


def solve(field):
    debug = False
    if debug:
        for row in field:
            print(row)

    maxcount = -1
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "T":
                # print('starting node {} {}'.format(row, col))
                count = dfs(row, col, field)
                # print('max count is {}'.format(count))
                # for r in field:
                # print(r)
                maxcount = count if count > maxcount else maxcount

    return maxcount


field = [['T', 'T', 'T', 'W', 'W'],
        ['T', 'W', 'W', 'T', 'T'],
        ['T', 'W', 'W', 'T', 'T'],
        ['T', 'W', 'T', 'T', 'T'],
        ['W', 'W', 'T', 'T', 'T']]

# for input use:
#n = int(input())
#field = []
#for i in range(n):
#    field.append(input().split(' '))
print(solve(field))