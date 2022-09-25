# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from utils import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # method-1:将值复制到数组中后用双指针法
        # 时间复杂度:O(n)
        # 空间复杂度:O(n)
        val = []
        curr = head
        while curr is not None:
            val.append(curr)
            curr = curr.next
        return val == val[::-1]

        # method-2:快慢指针法
        # 将后半部分链表反转
        # 时间复杂度:O(n)
        # 空间复杂度:O(1)
        if not head:
            return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        first, second = head, second_half_start
        while second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        first_half_end.next = self.reverse_list(second_half_start)
        return True

    # 快慢指针
    # 找到指针前半部分的尾部
    def end_of_first_half(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
















