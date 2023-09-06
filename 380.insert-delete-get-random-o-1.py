#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False
        # updates valToIndex
        index = self.valToIndex[val] # take val's index
        self.valToIndex[self.nums[-1]] = index # swap to last num's index 
        # update nums 
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # pop last num, which is val now
        self.nums.pop()
        # update valToIndex
        del self.valToIndex[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

