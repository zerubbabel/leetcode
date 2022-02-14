#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def toList(root):
            if root==None:return []
            return toList(root.left)+[root.val]+toList(root.right)
        a=toList(root)
        d={}
        for x in a:
            if k-x in d:
                return True
            else:
                d[x]=0
        return False
# @lc code=end

