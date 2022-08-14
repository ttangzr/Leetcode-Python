# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 09:34
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                # meet
                break
        if not fast or not fast.next:
            return None
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast
