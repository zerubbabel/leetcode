#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur=head
        d={}
        while cur and cur not in d:
            d[cur]=1
            cur=cur.next
        if cur==None:return False
        return True
# @lc code=end

