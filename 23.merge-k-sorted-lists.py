#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergerTwo(l1, l2):
            dummy = node = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    node.next =l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 or l2
            return dummy.next
        if not len(lists) or len(lists) == 0:
            return None
        while len(lists) > 1:
            list = mergerTwo(lists[0], lists[1])
            lists = [list]+lists[2:]
        return lists[0]
# @lc code=end

