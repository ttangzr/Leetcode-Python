# @Time    : 2020/6/19 20:59
# @Author  : T-
# @Site    : 
# @File    : 24-Swap Nodes in Pairs.py
# @Software: PyCharm

from utils import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode):
        # method-1:递归法
        # 从head开始，设置firstNode和secondNone两个结点，最后返回secondNode（新头）
        # 交换后的头是原始链表的第二个节点
        # 若无节点或只有一个节点
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next =  self.swapPairs(second.next)
        second.next = first
        return second

        # method-2:迭代法
        # 链表分奇数和偶数节点
        # prev为前节点的前驱节点
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first, second = head, head.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            head = first.next
        return dummy.next




















