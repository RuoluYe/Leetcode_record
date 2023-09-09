#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)
    def pop(self) -> None:
        
        self.stk.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

