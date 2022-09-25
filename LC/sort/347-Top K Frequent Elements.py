#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # method-1: quick sort/heap sort
        # 根据频次排序数组
        hashMap = dict()
        for num in nums:
            if hashMap.get(num) is not None:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        count = list(hashMap.items())    # key: num, val: count
        # heap sort
        top_k = self.heap_sort(count, k)
        # quick sort
        top_k = self.quick_sort(count, 0, len(count) - 1, len(count) - k)
        return [item[0] for item in top_k]
    
        # method-2: bucket sort
        count = dict()
        for num in nums:
            if count.get(num) is not None:
                count[num] += 1
            else:
                count[num] = 1
        # 根据频次分桶
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
                bucket[count].append(num)
        res = []
        for cnt in range(len(nums) - 1, 0, -1):
            if not bucket[cnt]:
                continue
            if len(res) < k:
                res += bucket[cnt]
            else:
                return res
        return res
    
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
        return nums[len(nums) - k:]

    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 <= heap_len - 1:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r][1] < heap[l][1]:
                nex = l
            else:
                nex = r
            if heap[p][1] < heap[nex][1]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def quick_sort(self, nums, left, right, index):
        p = self.partition(nums, left, right)
        if p == index:
            return nums[index:]
        elif p > index:
            self.quick_sort(nums, left, p - 1, index)
        else:
            self.quick_sort(nums, p + 1, right, index)

    def partition(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]

        pivot = nums[left][1]  # 频次为基准值
        lt = left
        # 循环不变量
        # all in [left + 1, lt] < pivot
        # all in [lt + 1, i) >= pivot
        for i in range(left + 1, right + 1):
            if nums[i][1] < pivot:  # 对比频次进行排序
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt


if __name__ == "__main__":
    obj = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    # nums = [1, 2]
    # k = 2
    # nums = [1]
    # k = 1
    print(obj.topKFrequent(nums, k))
