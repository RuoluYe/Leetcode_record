#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        # count = 1
        # from queue import Queue
        # q = Queue()
        # q.put(root)
        
        # while q:
        #     s = q.qsize()
        #     for i in range(s):
        #         cur = q.get()
        #         if not cur.left and not cur.right:
        #             return count
                
        #         if cur.left:
        #             q.put(cur.left)
        #         if cur.right:
        #             q.put(cur.right)
        #     count += 1 # update depth outside after examine all node at this level(after for loop ends)
        
        # return count
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return l+r+1 if l == 0 or r == 0 else min(l,r)+1
        
# @lc code=end

