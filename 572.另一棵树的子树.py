#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSame(root,subRoot):
            if root==None and subRoot==None:return True
            if root==None or subRoot==None:return False
            if root.val!=subRoot.val:return False
            return isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right)
        
        def isSon(root,subRoot):
            if root==None and subRoot==None:return True
            if root==None or subRoot==None:return False
            return isSame(root,subRoot) or isSon(root.left,subRoot) or isSon(root.right,subRoot)
            
        return isSon(root,subRoot)
# @lc code=end

