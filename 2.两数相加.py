#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        DummyHead=ListNode()
        cur=DummyHead
        c=0
        while l1 or l2 or c:
            t=ListNode()
            if l1:
                t.val+=l1.val
            if l2:
                t.val+=l2.val
            t.val+=c
            c=t.val//10
            t.val%=10
            cur.next=t
            if l1:l1=l1.next
            cur=cur.next
            if l2:l2=l2.next
        return DummyHead.next
# @lc code=end

