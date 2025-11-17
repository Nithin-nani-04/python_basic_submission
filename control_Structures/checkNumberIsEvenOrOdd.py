class Solution:
    def __init__(self,a):
        self.a=a
    def work(self):
        return 'odd' if self.a&1 else "even"
a=input("Enter the number: ")
s=Solution(int(a))
print(f"{a} is an {s.work()} number")