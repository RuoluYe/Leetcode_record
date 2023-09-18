#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        def sameTree(root, sub):
            if not (root and sub): # go in when any is None
            #if not root and not sub: # don't go in when one is None, only go in if both are None.
                return root is sub
            
            return (root.val == sub.val and
                    sameTree(root.left, sub.left) and 
                    sameTree(root.right, sub.right))
        if sameTree(root, sub):
            return True
        if not root:
            return False
        
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub) 

        
# @lc code=end

