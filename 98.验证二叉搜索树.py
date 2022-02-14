#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def toList(root):
            if root==None:return []
            return toList(root.left)+[root.val]+toList(root.right)
        a=toList(root)
        n=len(a)
        for i in range(1,n):
            if a[i]<=a[i-1]:
                return False
        return True
        
# @lc code=end

