# @Time    : 2020/6/19 20:13
# @Author  : T-
# @Site    : 
# @File    : 19-Remove Nth Node From End of List.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # method-1: 两次遍历算法
        # 删除从列表开头数起的第 (L−n+1) 个结点
        # 第一次遍历，找出L
        # 第二次遍历移动哑结点到 (L-n) 位置
        # 哑结点，用来简化极端情况，如只有一个结点，或需要删除列表头部
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        length = 0
        while p.next:
            length += 1
            p = p.next
        length -= n
        p = dummy
        while length > 0:
            length -= 1
            p = p.next
        p.next = p.next.next
        return dummy.next

        # method-2:一次遍历算法(头插法)
        # 使用双指针方法
        # 第一个指针从开头移动n+1，第二个指针从头出发(两个指针被n个结点分开）
        # 同时移动两个指针保持间隔，直到第一个指针到达最后一个结点，此时第二指针指向要删除的第n个结点
        # 哑结点
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        # slow, fast相差n
        while n > 0:
            n -= 1
            fast = fast.next
        # 移到末尾, slow下一个即为需删除节点
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next

        # method-3:栈
        # 根据栈「先进后出」的原则，我们弹出栈的第 n 个节点就是需要删除的节点
        dummy = ListNode(-1)
        dummy.next = head
        stack = []
        curr = dummy
        # 入栈
        while curr:
            stack.append(curr)
            curr = curr.next
        # 出栈
        while n + 1 > 0:  # pop到待删除节点的前一节点
            n -= 1
            curr = stack.pop()
        curr.next = curr.next.next
        return dummy.next














