#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:return []
        queue=[[root,0]]
        head,tail=0,1
        ans,t=[],[]
        while head<tail:
            cur=queue[head]
            if t==[] or queue[head-1][1]==cur[1]:
                t.append(cur[0].val)
            else:
                ans.append(t)
                t=[cur[0].val]
            if cur[0].left:
                queue.append([cur[0].left,cur[1]+1])
                tail+=1
            if cur[0].right:
                queue.append([cur[0].right,cur[1]+1])
                tail+=1
            head+=1
        if t!=[]:
            ans.append(t)
        return ans


# @lc code=end

