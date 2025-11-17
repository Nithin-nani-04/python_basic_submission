import math
class Solution:
    def __init__(self,a):
        self.a=a
    def work(self):
        print("Square root :", math.sqrt(self.a))
        print("Logarithm :",math.log(self.a))
        print("sine:",math.sin(self.a))
a=int(input("Enter the number:"))
s=Solution(a)
s.work()