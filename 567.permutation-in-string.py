#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        need,window = {}, {}
        for i in s1:
            need[i] = need.get(i,0)+1
        left,right = 0,0
        while right < len(s2):
            ch = s2[right]
            right += 1
            if ch in need:
                window[ch] = window.get(ch,0)+1
            while right - left >= len(s1):
                if window == need:
                    return True
                d = s2[left]
                left +=1
                if d in need:
                    window[d]-=1
                    if window[d] == 0:
                        window.pop(d)
        return False
                
                    
        
# @lc code=end

