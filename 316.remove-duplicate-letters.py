#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
         # 维护一个计数器记录字符串中字符的数量
        count = [0] * 256
        for i in range(len(s)):
            count[ord(s[i])]+=1
        instack = [False] * 256
        for c in s:
            # 每遍历过一个字符，都将对应的计数减一
            count[ord(c)]-=1
            if instack[ord(c)]:
                continue
            # "bcab", stk = [b], c = c, b !> c, so append (only append ord larger)
            # 'bcab', stk = [b,c], c = a, c > a, if no more this letter, break,
            # if more this letter (count[a]!= 0), instak[c] is false. stk[c] pop 
            # b > a, instack[b] is false, stk[b] pop
            # append a, instack[a] = true. 
            while len(stk) > 0 and stk[-1] > c:
                if count[ord(stk[-1])]== 0:
                    break
                instack[ord(stk.pop())] = False
            stk.append(c)
            instack[ord(c)] = True
        sb = []
        while len(stk) > 0:
            sb.append(stk.pop())
        return "".join(sb)[::-1]
# @lc code=end

