# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/12 9:34 PM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method: 分治
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return
        mid = (l + r) >> 1
        left_list = self.merge(lists, l, mid)
        right_list = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(left_list, right_list)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
