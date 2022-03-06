#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:return root
        q=[(root,0)]
        head,tail=0,0
        while head<=tail:
            cur=q[head]
            head+=1
            if cur[0].left:
                q.append((cur[0].left,cur[1]+1))
                tail+=1
            if cur[0].right:
                q.append((cur[0].right,cur[1]+1))
                tail+=1
        for i in range(tail):
            if q[i][1]==q[i+1][1]:
                q[i][0].next=q[i+1][0]
        return root

# @lc code=end

