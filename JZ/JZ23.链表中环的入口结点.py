'''
Description: 
Author: Zhirong
Date: 2022-02-21 20:50:54
LastEditTime: 2022-02-22 00:09:37
LastEditors: Zhirong
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # method-1: 双指针
        if not pHead:
            return None
        fast, slow = pHead, pHead
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:    # first meet
                break                
        if not fast or not fast.next:
            return None
        fast = pHead
        while fast != slow:     # second meet
            fast, slow = fast.next, slow.next
        return fast