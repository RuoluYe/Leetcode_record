#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        l, r =0, len(nums1) -1
        while True:
            i = (l+r) // 2
            # place at nums2
            j = half - i - 2
            Aleft = nums1[i] if i >= 0 else float('-inf')
            Aright = nums1[i+1] if i+1 < len(nums1) else float('inf')
            Bleft = nums2[j] if j>=0 else float('-inf')
            Bright = nums2[j+1] if j+1 < len(nums2) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                # odd total
                if total % 2: # is not 0
                    return min(Aright, Bright) # num, infinity
                # even
                return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft > Bright: # reduce size of A
                # shift r to i -1
                r = i-1
            else: # Bleft > Aright, more 
                l = i+1
                
# @lc code=end

