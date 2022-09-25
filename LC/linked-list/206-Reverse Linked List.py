# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """"""
        # method-1: 迭代法，prev为哨兵节点
        prev, curr = None, head
        # 遍历
        while curr:
            # 保存下个节点
            tmp = curr.next
            # 将当前结点指向prev
            curr.next = prev
            # prev和curr都前进一位
            prev = curr
            curr = tmp
            # curr.next, prev, curr = prev, curr, curr.next
        return prev

        # method-2: 递归法
        # 另nk.next.next = nk
        # 但要注意n1必须指向NULL
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next) # 返回新的头节点
        head.next.next = head
        head.next = None    # 断链，防止死循环
        return p


















