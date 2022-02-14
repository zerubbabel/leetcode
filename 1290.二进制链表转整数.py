#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=0
        while head:
            s=s*2+head.val
            head=head.next
        return s
        
# @lc code=end

