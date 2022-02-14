#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead=ListNode()
        dummyHead.next=head
        pre,cur=dummyHead,head
        while cur:
            if cur.val==val:
                pre.next=cur.next
                cur=pre.next
            else:
                pre,cur=cur,cur.next
        return dummyHead.next
# @lc code=end

