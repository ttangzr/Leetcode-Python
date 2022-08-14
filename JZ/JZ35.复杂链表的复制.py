'''
Description: 
Author: Zhirong
Date: 2022-02-22 09:54:39
LastEditTime: 2022-02-22 21:00:00
LastEditors: Zhirong
'''
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # method-1: hash map
        if not pHead:
            return None
        hashMap = dict()
        dummy = RandomListNode(-1)
        prev, curr = dummy, pHead
        while curr:
            clone = RandomListNode(curr.label)
            prev.next = clone
            hashMap[curr] = clone
            prev, curr = prev.next, curr.next
        for key, val in hashMap.items():
            val.random = None if key.random == None else hashMap[key.random]
        return hashMap[pHead]
    
        # method-2: 拼接、拆分
        if not pHead:
            return None
        curr = pHead
        # clone
        while curr:
            clone = RandomListNode(curr.label)
            clone.next = curr.next
            curr.next = clone
            curr = clone.next
        # deal with random    
        old, clone, ret = pHead, pHead.next, pHead.next
        while old:
            clone.random = None if old.random == None else old.random.next
            if old.next:
                old = old.next.next
            if clone.next:
                clone = clone.next.next
        # split
        old, clone = pHead, pHead.next
        while old:
            if old.next:
                old.next = old.next.next
            if clone.next:
                clone.next = clone.next.next
            old = old.next
            clone = clone.next
        return ret