#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        self.traverse(root,res)
        return res
    
    def traverse(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.traverse(root.left,res)
        self.traverse(root.right,res)
        
    
        
# @lc code=end

class Solution:
    # 动态规划思路
    # 定义：输入一个节点，返回以该节点为根的二叉树的前序遍历结果
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        # 前序遍历结果特点：第一个是根节点的值，接着是左子树，最后是右子树
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res

class Solution:
    # 回溯算法思路
    def __init__(self):
        self.res = []

    # 返回前序遍历结果
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        self.traverse(root)
        return self.res

    # 二叉树遍历函数
    def traverse(self, root: TreeNode) -> None:
        if not root:
            return
        # 前序遍历位置
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)