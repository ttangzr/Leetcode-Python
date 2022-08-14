# @Time    : 2020/6/18 15:45
# @Author  : T -
# @Site    : 
# @File    : 160. Intersection of Two Linked Lists.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Get the intersection of two linked lists.

        Args:
            headA: ListNode1
            headB: ListNode2

        Returns:
            Intersection node.
        """
        # method-1: 双指针法
        # a + b + c = b + a + c
        # 移动至尾部后重新将指针指向另一链表开始移动，到公共结点时pA = pB，就获取到了公共结点
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


