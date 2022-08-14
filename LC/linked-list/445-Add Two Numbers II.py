# @Time    : 2020/6/22 14:15
# @Author  : T-
# @Site    : 
# @File    : 445-Add Two Numbers II.py
# @Software: PyCharm

from utils import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
            
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            val = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            cur_node = ListNode(val)
            cur_node.next = ans
            ans = cur_node
        return ans
        
        # method-1:栈
        # 把所有数字压入栈中，再依次取出相加，注意进位问题
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0

        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            curr = a + b + carry
            carry = curr // 10  # 进位
            curr %= 10          # 个位
            curr_node = ListNode(curr)
            curr_node.next = ans
            ans = curr_node

        return ans

