#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    # O(n), O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        
        # maxf should never decrement since maxf+k is the longest
        # maxf = max(count.values)
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if (r-l+1)- maxf > k: # too long, left shrink
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
                
        return res        
    
# @lc code=end

# O(26n), O(n)
  def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
            # If a character is in the dict, we simply add one.
            freq[s[r]] = freq.get(s[r], 0) + 1
             
            # The key point is that we only care about the MAXIMUM of the seen values.
            # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
            cur_len = r - l + 1
            if cur_len - max(freq.values()) <= k:  # if we have replaced <= K letters, record a new maxLen
                maxlen = max(maxlen, cur_len)
            else:                               # if we have replaced > K letters, then it's time to slide the window
                freq[s[l]] -= 1                 # decrement frequency of char at left pointer, then increment pointer
                l += 1
               
        return maxlen
