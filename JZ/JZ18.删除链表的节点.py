'''
Description: 
Author: Zhirong
Date: 2022-02-22 09:46:06
LastEditTime: 2022-02-22 09:52:35
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
# @param head ListNode类 
# @param val int整型 
# @return ListNode类
#
class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        if not head:
            return None
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                break
            curr = curr.next
        return dummy.next