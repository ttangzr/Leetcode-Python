# @Time    : 2020/6/19 17:34
# @Author  : T-
# @Site    : 
# @File    : 83-Remove Duplicates from Sorted List.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # method-1:递归法
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head.next = head.next.next
        return head

        # method-2:直接法
        curr = head
        while cur and cur.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


