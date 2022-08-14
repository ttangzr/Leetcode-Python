# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 15:12

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.dummy = ListNode(-1)

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        cur = self.dummy
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index < 0:
            index = 0
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == "__main__":
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)

    linkedList.addAtIndex(1, 2) # 链表变为1-> 2-> 3
    linkedList.get(1)           # 返回2
    linkedList.deleteAtIndex(1) # 现在链表是1-> 3
    linkedList.get(1)           # 返回3