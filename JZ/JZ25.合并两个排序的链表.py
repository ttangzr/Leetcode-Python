'''
Description: 
Author: Zhirong
Date: 2022-02-21 15:52:15
LastEditTime: 2022-02-21 19:46:55
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
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        # method-1: 双指针/迭代
        dummy = ListNode(-1)
        prev = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                prev.next = pHead1
                pHead1 = pHead1.next
            else:
                prev.next = pHead2
                pHead2 = pHead2.next
            prev = prev.next
        # Merge reset listNode
        prev.next = pHead1 if pHead1 else pHead2
        return dummy.next
    
        # method-2: 递归/DFS
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        elif pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
        
            