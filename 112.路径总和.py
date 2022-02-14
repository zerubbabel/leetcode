#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        
        def ok(root,targetSum):
            if root==None:return False
            if root.left==None and root.right==None:
                return root.val==targetSum
            else:
                return ok(root.left,targetSum-root.val) or ok(root.right,targetSum-root.val)
        return ok(root,targetSum)
# @lc code=end

