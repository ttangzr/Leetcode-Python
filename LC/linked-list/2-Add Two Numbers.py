# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/17 20:28
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                carry = val // 10
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                val = l1.val + carry
                carry = val // 10
                l1 = l1.next
            elif l2 and not l1:
                val = l2.val + carry
                carry = val // 10
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
        if carry != 0:  # 额外的进位
            curr.next = ListNode(carry)
        return dummy.next

if __name__ == "__main__":
    obj = Solution()
    l1_ = [ListNode(9), ListNode(9), ListNode(9)]
    l2_ = [ListNode(9)]
    for i in range(len(l1_) - 1):
        l1_[i].next = l1_[i + 1]
    for i in range(len(l2_) - 1):
        l2_[i].next = l2_[i + 1]
    obj.addTwoNumbers(l1_[0], l2_[0])