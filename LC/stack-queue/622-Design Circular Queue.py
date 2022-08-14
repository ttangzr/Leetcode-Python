# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 10:31

from threading import Lock
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        # tail = (head + count - 1) % capacity
        self.count = 0
        self.capacity = k
        self.lock = Lock()

    def enQueue(self, value: int) -> bool:
        # self.lock.acquire() 
        if self.isFull():
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        # self.lock.release()
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3)
    circularQueue.enQueue(1)    # true
    circularQueue.enQueue(2)    # true
    circularQueue.enQueue(3)    # true
    circularQueue.enQueue(4)    # false
    print(circularQueue.Rear())        # 3
    circularQueue.isFull()      # true
    circularQueue.deQueue()     # true
    circularQueue.enQueue(4)    # true
    circularQueue.Rear()        # 4