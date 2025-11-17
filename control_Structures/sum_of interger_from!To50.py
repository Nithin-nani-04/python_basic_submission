class Solution:
    def work(self):
        su=0
        for i in range(1,51,1):
            su+=i
        return su
s=Solution()
print(f"The sum of numbers from 1 to 50 is: {s.work()}")