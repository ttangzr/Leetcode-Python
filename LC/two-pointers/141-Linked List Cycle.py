#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 11:17 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 141-Linked List Cycle.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False