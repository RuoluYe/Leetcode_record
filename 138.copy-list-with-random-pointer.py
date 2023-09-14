#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # 难点：前方的node.random是还没有被initialize的后方
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldcopy = {None: None}
        cur = head
        # store all copy of nodes in a hashmap
        # {[7,null]:[7],
        #   [13,0]:[13],...}
        while cur:
            copy = Node(cur.val)
            oldcopy[cur] = copy
            cur = cur.next
        cur = head
        # put .next for each copy according to their next and random
        while cur:
            copy = oldcopy[cur]
            copy.next = oldcopy[cur.next]
            copy.random = oldcopy[cur.random]
            cur = cur.next
            
        return oldcopy[head]
# @lc code=end

