#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # method-1: quick sort
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

        # method-2: heap sort
        # recommended bit root heap
        return self.heap_sort(nums, k)

        # python heap library - big root heap
        heap = []
        for num in nums:
            import heapq
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        # [class Heap] heap sort  - small root heap
        heap = Heap(k + 1)
        for num in nums:
            if not heap.push(num):
                heap.pop()
                heap.push(num)
        if heap.size == k + 1:
            heap.pop()
        return heap.peak()

    def quick_select(self, nums, left, right, index):
        q = self.partition(nums, left, right)
        # divide-and-conquer
        if q == index:
            return nums[q]
        elif q > index:
            return self.quick_select(nums, left, q - 1, index)
        else:
            return self.quick_select(nums, q + 1, right, index)

    def partition(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]

        pivot = nums[left]     # 基准值
        lt = left
        # 循环不变量
        # all in [left + 1, lt] < pivot
        # all in [lt + 1, i) >= pivot
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt

    # 堆排序
    def heap_sort(self, nums, k):
        # 初始化堆
        for i in range(len(nums) - 1, -1, -1):
            self.max_heapify(nums, i, len(nums))
        # 交换元素
        for i in range(len(nums) - 1, len(nums) - k - 1, -1):
            # 末尾元素与堆顶交换
            nums[i], nums[0] = nums[0], nums[i]
            # 调整堆使剩余元素仍为大根堆
            self.max_heapify(nums, 0, i)
        return nums[len(nums) - k]

    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 <= heap_len - 1:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

# not recommended
class Heap(object):
    # 小根堆
    def __init__(self, length):
        self.heap = [0] * (length + 1)
        self.size = 0

    def push(self, val):
        if self.size == len(self.heap) - 1:
            return False
        self.size += 1
        self.heap[self.size] = val
        self.shift_up(self.size)
        return True

    def pop(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.shift_down(1)
        return val

    def peak(self):
        return self.heap[1]

    def shift_up(self, i):
        val = self.heap[i]
        while i >> 1 > 0:
            parent = i >> 1
            if val < self.heap[parent]:
                self.heap[i] = self.heap[parent]
                i = parent
            else:
                break
        self.heap[i] = val

    def shift_down(self, i):
        val = self.heap[i]
        while i << 1 <= self.size:
            child = i << 1
            if child != self.size \
                    and self.heap[child + 1] < self.heap[child]:
                child += 1
            if val > self.heap[child]:
                self.heap[i] = self.heap[child]
                i = child
            else:
                break
        self.heap[i] = val


if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(obj.findKthLargest(nums, k))