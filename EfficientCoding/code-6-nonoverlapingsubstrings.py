class nonOverlapingString:
    def __init__(self):
        self.count = 0


    def solve(self, str, start, out):
        if start == len(str):
            print(out[:-1])
            self.count += 1

        for idx in range(start, len(str)):
            output = str[start: idx+1] + ","
            newOutput = out+output
            self.solve(str, idx+1, newOutput)

        return self.count

str = "ABCD"
start = 0
out = ""
obj = nonOverlapingString()
print(obj.solve(str, start, out))