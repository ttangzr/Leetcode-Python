# @Time    : 2020/6/18 17:14
# @Author  : T-
# @Site    : 
# @File    : 21-Merge Two Sorted Lists.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # method-1: 递归法
        # 头部较小的节点与剩下的元素merge合并
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        # method-2: 迭代
        # l1和l2非空时，判断两者哪一更小，则将较小的添加到结果，对应链表的节点后移一位
        # 哨兵节点
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 合并后l1和l2两者最多只有一个没有合并完，只需要将链表的末尾指向其即可
        prev.next = l1 if l1 else l2
        return dummy.next
