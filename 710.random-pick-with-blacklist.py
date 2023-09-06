#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#

# @lc code=start
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.sz = n - len(blacklist)
        self.mapping = {}# a hashmap b to other index
        for b in blacklist:
            self.mapping[b] = 999       
        
        last = n - 1
        for b in blacklist:
            if b >= self.sz: # b will not get picked
                continue
            # get an unused index & make sure last is not in blacklist
            while last in self.mapping: 
                last -= 1
            # mapping[b] return the index
            self.mapping[b] = last
            last -= 1                

    def pick(self) -> int:
        import random
        index = random.randint(0, self.sz-1)
        if index in self.mapping: # blacklist got picked
            return self.mapping[index] # get the index that is map to that blacklist
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

