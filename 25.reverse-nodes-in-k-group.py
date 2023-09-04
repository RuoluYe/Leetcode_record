#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        a = b = head
        # check kth
        for i in range(k):
            if not b:
                return head
            b = b.next
        #rever kth
        newHead = self.reverse(a,b)
        #connect the recursion of the continuous list
        a.next = self.reverseKGroup(b,k) # a is the start of the last list, the end of the reverse list, reverse from b now. 
        return newHead # the reverse list: from b to a.                                              
    def reverse(self, a, b): 
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
# @lc code=end

