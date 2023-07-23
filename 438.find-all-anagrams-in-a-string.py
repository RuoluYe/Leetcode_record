#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
        if len(t) > len(s):
            return[]
        
        need, window = {}, {}
        for i in range(len(t)):
            need[t[i]] = 1+need.get(t[i],0)
            window[s[i]] = 1+window.get(s[i],0)
            
        res = [0] if need == window else []
        l = 0
        for r in range(len(t), len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            window[s[l]] -= 1
            
            if window[s[l]] == 0:
                window.pop(s[l])
            l+=1
            if window==need:
                res.append(l)
        

        return res
            
                
            
# @lc code=end

