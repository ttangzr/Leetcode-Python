# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 10:31

class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.queue = [0] * (k + 1)    # capacity + 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[(self.rear - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front == ((self.rear + 1) % len(self.queue))


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