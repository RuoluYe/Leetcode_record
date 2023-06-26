#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxD = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.traverse(root)
        return self.maxD
    def traverse(self, root):
        if not root:
            return 0
        leftMax = self.traverse(root.left)
        rightMax = self.traverse(root.right)
        self.maxD = max(self.maxD, leftMax+rightMax) # update maxD after getting the left & right max of this node
        return 1+max(leftMax,rightMax) # return the max depth from this node
        
        
# @lc code=end

