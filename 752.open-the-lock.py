  #
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus(s, j):
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = chr(ord(ch[j])+1)
            return ''.join(ch)
        def minus(s, j):
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = chr(ord(ch[j])-1)
            return ''.join(ch)
            
        
        visited = set()
        deads = set(deadends)
        from collections import deque
        q = deque()
    
        q.append("0000")
        visited.add("0000")
        step = 0
        
        while q:
            sz = len(q)
            # current 
            for i in range(sz):
                cur = q.popleft()
                
                # determine
                if cur in deads:
                    continue
                if cur == target:
                    return step
                
                for j in range(4):
                    up = plus(cur,j)
                    down = minus(cur,j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            # after for loop, examined all nodes in this step
            step += 1
        
        return -1   
        
        
        
# @lc code=end

