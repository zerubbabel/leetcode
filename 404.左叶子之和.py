#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None:return 0
        def getLeft(root,left):
            if root==None:return 0
            if root.left==None and root.right==None and left: return root.val
            return getLeft(root.left,1)+getLeft(root.right,0)

        return getLeft(root.left,1)+getLeft(root.right,0)
# @lc code=end

