# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/12 9:34 PM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method-1: 分治
        return self.merge(lists, 0, len(lists) - 1)
    
        # method-2: 优先队列/小根堆
        dummy = ListNode(-1)
        p = dummy
        que = []
        # 入队列
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(que, [lists[i].val, i])
                lists[i] = lists[i].next
        # 出队列
        while que:
            # 先出为最小
            val, idx = heapq.heappop(que)
            # 建链
            p.next = ListNode(val)
            p = p.next
        return dummy.next
            

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
