#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root==[]:return []
        if root:
            ans=[root.val]
            for x in root.children:
                if x:ans+=self.preorder(x)
            return ans
        
# @lc code=end

