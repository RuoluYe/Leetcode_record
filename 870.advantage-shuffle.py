#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
class Solution:
    import heapq
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        maxpq = [(-val, i) for i, val in enumerate(nums2)]
        self.heapq.heapify(maxpq)
        nums1.sort()
        
        left,right = 0,  n-1
        res = [0] * n
        while maxpq:
            val, i = self.heapq.heappop(maxpq)
            maxval = -val # largest num in nums2
            if maxval < nums1[right]:
                res[i] = nums1[right] # right vs. nums2[i]
                right -= 1
            else:
                res[i] = nums1[left] # let min vs. nums2[i]
                left += 1
        return res
            
                
# @lc code=end

我们暂且把田忌的一号选手称为 T1，二号选手称为 T2，齐王的一号选手称为 Q1。

如果 T2 能赢 Q1，你试图保存己方实力，让 T2 去战 Q1，把 T1 留着是为了对付谁？

显然，你担心齐王还有战力大于 T2 的马，可以让 T1 去对付。

但是你仔细想想，现在 T2 已经是可以战胜 Q1 的，Q1 可是齐王的最快的马，齐王剩下的那些马里，没有比 T2 更强的马。

所以，没必要节约，最后我们得出的策略就是：

将齐王和田忌的马按照战斗力排序，然后按照排名一一对比。如果田忌的马能赢，那就比赛，如果赢不了，那就换个垫底的来送人头，保存实力。