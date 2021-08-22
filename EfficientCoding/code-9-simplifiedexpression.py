def simplified(expr):
    idx = 0
    while True:
        char = expr[idx]
        if char == "(":
            previouschar = expr[idx-1]
            start = idx
            count = 1
            plusLoc = []
            minusLoc = []
            for i in range(idx+1, len(expr)):
                nextChar = expr[i]

                if nextChar == "(":
                    count += 1
                elif nextChar == ")":
                    count -= 1
                elif nextChar == "+" and count == 1:
                    plusLoc.append(i)
                elif nextChar == "-" and count == 1:
                    minusLoc.append(i)

                if count == 0:
                    #print("found end at {}".format(i))
                    end = i-1

                    if previouschar == "-":
                        # Switch signs
                        for plus in plusLoc:
                            expr[plus] = "-"
                        for minus in minusLoc:
                            expr[minus] = "+"

                    # Remove braces
                    if start-1 >= 0:
                        expr = expr[:start] + expr[start+1:]
                    if end < len(expr):
                        #print(expr[:end])
                        #print(expr[end+1:])
                        expr = expr[:end] + expr[end+1:]

                    # Stop loop & move to next char
                    break

            #print("new modified expr is {}".format(expr))

        idx += 1
        if idx >= len(expr):
            break

    return expr


expr = "a-(b-c-(d+e))-f"
res = simplified(list(expr))
print("".join(res))