'''
Description: 
Author: Zhirong
Date: 2022-02-22 21:01:57
LastEditTime: 2022-02-22 21:32:25
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
# @return ListNode类
#
class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        if not pHead:
            return None
        hashMap = dict()
        curr = pHead
        # mark duplicates
        while curr:
            if hashMap.get(curr.val) is not None:
                hashMap[curr.val] = 1
            else:
                hashMap[curr.val] = 0
            curr = curr.next
        # delete duplicates
        dummy = ListNode(-1)
        dummy.next = pHead
        prev, curr = dummy, pHead
        while curr:
            if hashMap[curr.val]:
                curr = curr.next
                prev.next = curr
            else:
                prev, curr = curr, curr.next
        return dummy.next
        