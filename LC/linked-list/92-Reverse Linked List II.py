# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/18 21:00
# Definition for singly-linked list.
from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # method-1: 迭代(两次遍历)
        if not head or left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head # pointer
        cnt = 1
        # 确定prev_node, succ_node, l_node, r_node
        while cur:
            if cnt == left:
                l_node = cur
                prev_node = prev
            elif cnt == right:
                r_node = cur
                succ_node = cur.next
                break
            prev, cur = cur, cur.next
            cnt += 1
        # 断链
        prev_node.next = None
        r_node.next = None
        # 反转left->right链表
        self.reverseList(l_node)
        # 建新链
        prev_node.next = r_node
        l_node.next = succ_node
        return dummy.next
    
        # method-2: 迭代(一次遍历)
        if not head or left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next     # cur保持不动
        for _ in range(left, right):
            nex = cur.next
            cur.next = nex.next
            nex.next = prev.next
            prev.next = nex
        return dummy.next 
        
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        


