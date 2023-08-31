#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        
        window = defaultdict(int)
        count = 0
        left, right = 0,0
        start, length = 0, float('inf')
        
        while right < len(s): #loop thru s
            c = s[right]
            right += 1
            if c in need: 
                window[c] += 1
                if window[c] == need[c]: # meet need for c
                    count += 1
            
            # when count = len(t)
            while count == len(need):
                # update substring size
                # record the last possible substring 
                if (right - left)  < length:
                    start = left
                    length = right - left
                
                # check shrinking left & extends right to find smaller possible substring    
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        count -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start:start+end]
                    
        
        
            
# @lc code=end

# 1. 计数 need
# 2. 窗口开闭 left right


# 思考：
# 1、什么时候应该移动 right 扩大窗口？窗口加入字符时，应该更新哪些数据？

# 2、什么时候窗口应该暂停扩大，开始移动 left 缩小窗口？从窗口移出字符时，应该更新哪些数据？

# 3、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？

# 如果一个字符进入窗口，应该增加 window 计数器；
# 如果一个字符将移出窗口的时候，应该减少 window 计数器；
# 当 valid 满足 need 时应该收缩窗口；应该在收缩窗口的时候更新最终结果。




