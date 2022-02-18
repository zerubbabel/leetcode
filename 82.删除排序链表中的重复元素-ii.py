#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        dummyhead=ListNode()
        dummyhead.next=head
        pre=dummyhead
        while head and head.next:
            if head.next.val==head.val:
                while head and head.next and head.next.val==head.val:
                    head=head.next
                pre.next=head.next
                head=head.next
            else:
                pre,head=head,head.next
        return dummyhead.next
        
# @lc code=end

