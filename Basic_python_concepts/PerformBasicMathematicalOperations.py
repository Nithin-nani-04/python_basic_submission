class Solution:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def work(self):
        print("Addition:", self.a+self.b)
        print("Subtraction:",self.a-self.b)
        print("multiplication:",self.a*self.b)
        print("Division:",self.a/self.b)
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
s=Solution(a,b)
s.work()