# @Time    : 2020/6/22 16:55
# @Author  : T-
# @Site    : 
# @File    : 328-Odd Even Linked List.py
# @Software: PyCharm

from ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # method-1:双指针
        if not head:
            return None
        odd, even = head, head.next
        even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head