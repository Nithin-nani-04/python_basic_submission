class Solution:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def work(self):
        print(f"Hello, {self.a} {self.b}! Welcome to Python program")
a=input("Enter the first name: ")
b=input("Enter the last name: ")
s=Solution(a,b)
s.work()