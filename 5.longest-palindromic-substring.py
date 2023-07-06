#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # need to check l>=0 first, otherwise s[l] throw IndexOutOfBound
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i+1) # for same 2 letters at the center like 'baab'
            if len(res) < len(s1):
                res = s1
            if len(res) < len(s2):
                res = s2
        return res
        
        
        
# @lc code=end

