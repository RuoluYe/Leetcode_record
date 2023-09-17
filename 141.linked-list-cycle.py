#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next: # while fast and fast.next
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
# @lc code=end

