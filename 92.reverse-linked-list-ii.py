#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def __init__(self):
            self.successor = None
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            last = reverseN(head.next, n-1) #前进到第n个
            head.next.next = head # reverse arrow
            head.next = self.successor 
            return last
        if left == 1:
            return reverseN(head, right) # 反转 left 到 right
        head.next = self.reverseBetween(head.next, left-1, right-1) # this return the reverse linked-list when left = 1
        return head
# @lc code=end

# traversal

def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        # 1. reach node at position left.  
        for i in range(left-1):
            prev, cur = cur, cur.next 

        # prev = node before left, cur = left
        # 2. reverse from left to right
        before = None
        for i in range(left, right+1):
            after = cur.next
            cur.next = before
            before, cur = cur, after
        
        prev.next.next=cur
        prev.next = before
        return dummy.nexts
