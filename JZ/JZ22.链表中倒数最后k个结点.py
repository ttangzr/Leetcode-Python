'''
Description: 
Author: Zhirong
Date: 2022-02-22 09:15:01
LastEditTime: 2022-02-22 09:36:59
LastEditors: Zhirong
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int):
        # write code here
        # method-1: stack
        if not pHead:
            return None
        stack = list()
        while pHead:
            stack.append(pHead)
            pHead = pHead.next
        if k > len(stack):
            return None
        res = None
        while k:
            res = stack.pop()
            k -= 1
        return res
    
        # method-2: 双指针
        if not pHead:
            return None
        slow, fast = pHead, pHead
        while k:
            if not fast:
                return None
            fast = fast.next
            k -= 1
        while fast:
            slow, fast = slow.next, fast.next
        return slow
        