#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalilndrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def alphanum(c):
            return (ord("A") <= ord(c) <= ord("Z") 
                or ord("a") <= ord(c) <= ord("z") 
                or ord("0") <= ord(c) <= ord("9")
                )
        while l < r:
            while l < r and not alphanum(s[l]):
                l+=1
            while l < r and not alphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
                    
# @lc code=end

