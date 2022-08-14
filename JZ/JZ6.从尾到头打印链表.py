# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/20 11:37 PM

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param listNode ListNode类
# @return int整型一维数组
#
class Solution:
    def __init__(self):
        self.res = list()
        
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        # method-1: force
        res = list()
        p = listNode
        if not p:
            return []
        while p:
            res.append(p.val)
            p = p.next
        return res[::-1]

        # method-2: 递归/DFS
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.res.append(listNode.val)
        return self.res
    
        # method-3: stack
        if not listNode:
            return []
        stack = list()
        res = []
        p = listNode
        while p:    # 进栈
            stack.append(p.val)
            p = p.next
        while stack:  # 出栈
            res.append(stack.pop())
        return res
        
        
        