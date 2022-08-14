# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/9 8:14 PM
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            tail = prev
            # 查看剩余长度是否大等于k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            # 保存下一个开始
            nex = tail.next
            # 反转k个
            head, tail = self.reverse(head, tail)
            # 把子链表接回原链表
            prev.next, tail.next = head, nex
            # 计算下一组k
            prev = tail
            head = tail.next
        return dummy.next

    def reverse(self, head, tail):
        prev, cur = None, head
        while prev != tail:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return tail, head

