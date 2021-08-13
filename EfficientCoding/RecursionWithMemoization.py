class RecuWMemo:
    def __init__(self):
        self.memory = [0, 1]

    def fib_slow(self, n):
        if n <= 1:
            return n
        else:
            return self.fib_slow(n-1) + self.fib_slow(n-2)

    def fib_mem(self, n):
        if n < len(self.memory):
            return self.memory[n]
        else:
            #print(n)
            self.memory.append(self.fib_mem(n-1) + self.fib_mem(n-2))
            #print("Updated {}".format(self.memory))

        return self.memory[n]

    def fib_dp(self, n):
        memory = [0] * n
        memory[0:2] = [1,1]
        if n < 2:
            return n
        for i in range(2, n):
            memory[i] = memory[i-1] + memory[i-2]

        return memory[n-1]

    def fib_dp2(self, n):
        memory = [1, 1]
        if n < 2:
            return n
        for i in range(2, n):
            temp = memory[1]
            memory[1] = memory[0] + memory[1]
            memory[0] = temp

        return memory[1]



r = RecuWMemo()
n1 = 40
#print(r.fib_slow(n))
print(r.fib_mem(n1))

print(r.fib_dp(n1))

print(r.fib_dp2(n1))