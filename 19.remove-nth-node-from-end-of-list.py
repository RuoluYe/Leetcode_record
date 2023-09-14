#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l, r = dummy, head
        
        for i in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
        
# @lc code=end

