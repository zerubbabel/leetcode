#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(root,son):
            a=[]
            cur=root
            while 1:
                a.append(cur)
                if cur.val==son.val:break
                if son.val<cur.val:
                    cur=cur.left
                else:
                    cur=cur.right
            return a
        pa=find(root,p)
        qa=find(root,q)
        m=min(len(pa),len(qa))
        i=0
        while i<m and pa[i]==qa[i]:
            i+=1
        return pa[i-1]
        

# @lc code=end

