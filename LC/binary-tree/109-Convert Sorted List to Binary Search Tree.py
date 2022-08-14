#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/13 8:36 上午
# @Author  : T-
# @Site    : 
# @File    : 109-Convert Sorted List to Binary Search Tree.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode):
        # method-1: 双指针/快慢指针
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        # 断开前后链表
        pre.next = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

        # method-2: 分治
        def getMedian(left: ListNode, right: ListNode):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def buildTree(left: ListNode, right: ListNode):
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)