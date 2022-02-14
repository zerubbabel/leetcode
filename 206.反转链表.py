#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        pre,cur=None,head
        while cur!=None:
            t=cur.next
            cur.next=pre
            pre,cur=cur,t
        return pre

# @lc code=end

