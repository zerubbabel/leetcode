#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:return TreeNode(val)
        cur=root
        while cur:
            if val<cur.val:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    break
            else:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    break
        return root
        



# @lc code=end

