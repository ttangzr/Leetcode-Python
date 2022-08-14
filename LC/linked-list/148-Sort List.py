# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/18 20:33

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # 注意单个node情况
            return head
        # 二分链表
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # 断链
        mid = slow.next
        slow.next = None
        # 合并链表
        left, right = self.sortList(head), self.sortList(mid)
        return self.mergeTwoList(left, right)
        
    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1, l2.next)
            return l2