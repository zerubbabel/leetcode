#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:return head
        pre,cur=head,head.next
        while cur:
            if cur.val==pre.val:
                pre.next=cur.next
                cur=pre.next
            else:
                pre,cur=cur,cur.next
        return head
# @lc code=end

