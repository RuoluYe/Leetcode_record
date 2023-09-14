#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # second half of the list
        prev = slow.next = None
        #reverse the second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
        
        # merge
        first, second = head, prev
        while second:
            tmp = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp
            first, second = tmp, tmp2      
        
        
# @lc code=end

