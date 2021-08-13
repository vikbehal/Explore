class StairCase:
    def __init__(self, k):
        self.k = k

    def num_ways(self, n):
        if n == 0:
            return 1
        total = 0
        for i in self.k:
            if n - i >= 0:
                total += self.num_ways(n - i)

        return total

    def num_ways2(self, n):
        if n == 0:
            return 1
        nums = [1]
        for i in range(1, n+1):
            #print("processing {}".format(i))
            total = 0
            for j in self.k:
                if i - j >= 0:
                    total += nums[i-j]

            nums.append(total)
            print(nums)

        print("All ways {}".format(nums))
        return nums[n]


k = [1, 3, 5]
n = 10
s1 = StairCase(k)
#print(s1.num_ways(n))
print(s1.num_ways2(n))
