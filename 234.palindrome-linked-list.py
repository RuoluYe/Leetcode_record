#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        # when while loop ends, 
        # fast -> last node(ListNode, odd) 
        #      or last node.next(null, even)
        # slow -> palindrome start (even)
        # slow -> center of the list (odd)
        if fast != None: # odd
            slow = slow.next #move next to the odd center
            
        #reverse slow:end, right = the new head of the reverse linked (used to be the last node)
        left, right = head, self.reverse(slow)
        while right:
            # compare the first and the "last"
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
    def reverse(self,head):
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
            
# @lc code=end

