# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from ListNode import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # method-1: create
        cur = head
        N = 0   # num of nodes
        while cur:
            N += 1
            cur = cur.next
        cur = head  # reset
        width, rem = N // k, N % k
        res = []
        for i in range(k):
            dummy = node = ListNode(None)
            # rem: 需要多余node的list数
            for j in range(width + (i < rem)):
                node.next = ListNode(cur.val)
                print(cur.val)
                node = node.next
                cur = cur.next
            res.append(dummy.next)
        return res
    
        # method-2: split
        cur = head
        N = 0   # num of nodes
        while cur:
            N += 1
            cur = cur.next
        cur = head  # reset
        width, rem = N // k, N % k
        res = []
        for i in range(k):
            head = cur
            for j in range(width + (i < rem) - 1):
                # 移动至当前segment最后一个node
                cur = cur.next
            if cur:
                # 断链
                cur.next, cur = None, cur.next
            res.append(head)
        return res


if __name__ == "__main__":
    root = ListNode(None)
    root.append(1)
    root.append(2)
    root.append(3)
    root.append(4)
    root.append(5)
    k = 2
    obj = Solution()
    res = obj.splitListToParts(root.head, k)

