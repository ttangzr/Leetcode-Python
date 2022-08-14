# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/9 7:11 PM

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # hash map: store key-value pairs
        self.cache = dict()
        # dummy head and tail
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        # link head tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 定位
        node = self.cache[key]
        # 更新移动到head
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # key not exists
            node = DLinkedNode(key, value)
            # add to hashmap
            self.cache[key] = node
            # add to head
            self.addToHead(node)
            self.size += 1
            # oversize
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # key exists, find it in hashmap and update
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    obj = LRUCache(2)
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.put(3, 3))
    print(obj.get(2))
    print(obj.put(4, 4))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))