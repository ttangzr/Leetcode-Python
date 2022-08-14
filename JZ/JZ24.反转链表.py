'''
Description: 
Author: Zhirong
Date: 2022-02-21 15:11:34
LastEditTime: 2022-02-21 15:12:51
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
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        # method-1:双指针/迭代
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev    # reverse
            prev = curr         # move two pointer forward
            curr = tmp
            # equal to:
            # curr.next, prev, curr = prev, curr, curr.next
        return prev
    
        # method-1: 递归
        if head == None or head.next == None:
            return head
        p = self.ReverseList(head.next)
        head.next.next = head
        head.next = None
        return p