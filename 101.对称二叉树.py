#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import fabs


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:return True
        
        def dfs(left,right):
            if left==None and right==None:return True
            if left==None or right==None:return False
            if left.val!=right.val:return False

            return dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)

# @lc code=end

