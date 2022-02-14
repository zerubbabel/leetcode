#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    a,b=[],[]
    def __init__(self):
        self.a,self.b=[],[]

    def push(self, x: int) -> None:
        while len(self.b):
            self.a.append(self.b.pop())
        self.a.append(x)

    def pop(self) -> int:
        while len(self.a):
            self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        while len(self.a):
            self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        return len(self.a)==0 and len(self.b)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

