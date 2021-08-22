### Does not work
### check this
### https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/samu-and-shooting-game/
### check below code and screenshot for explanation


def abbreviation(a, b, i=0, j=0, checked=None):
    checked = set() if checked is None else checked  # 1
    if j == len(b):  # 2
        more_uppers = any(char.isupper() for char in a[i:])
        return "NO" if more_uppers else "YES"
    for k in range(i, len(a)):  # 3
        if a[k].isupper() and a[k] != b[j]:  # 4
            return "NO"
        if a[k].upper() == b[j]:  # 5
            if (k, j) in checked:  # 6
                pass
            elif abbreviation(a,b,k+1,j+1,checked) == "YES":  # 7
                return "YES"
            else:
                checked.add((k, j))
            if a[k].isupper():  # 8
                return "NO"
    return "NO" # 9


for _ in range(int(input())):
    str_one = input()
    str_two = input()
    found = False

    if len(str_two) > len(str_one):
        print("NO")
    else:
        if dp(str_one, str_two):
            print("YES")
        else:
            print("NO")
