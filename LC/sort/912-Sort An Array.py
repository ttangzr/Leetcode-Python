# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 9:27 AM

from typing import List


class Solution:
    def sortArray(self, nums: List[int]):
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    # 冒泡排序
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n - 1, -1, -1):
            sorted = True   # ends if sorted
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    sorted = False
            if sorted: break
        return nums

    # 选择排序
    def select_sort(self, nums):
        n = len(nums)
        # 循环不变量：[0, i)有序
        for i in range(n - 1):
            # 选择[i, n - 1]最小元素索引，交换到i
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    # 插入排序
    def insert_sort(self, nums):
        n = len(nums)
        # 循环不变量：将nums[i]插入[0,i)使之有序
        for i in range(1, n):
            # 暂存该元素
            temp = nums[i]
            # 将i之前的元素逐个后移，留出空位给nums[i]
            j = i
            while j > 0 and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp
        return nums

    # 希尔排序
    def shell_sort(self, nums):
        n = len(nums)
        h = 1
        # 使用 Knuth 增量序列, 找增量的最大值
        while 3 * h + 1 < n:
            h = 3 * h + 1
        # 将nums[i]插入正确位置，将间隔1改为gap
        def insert_delta(nums, gap, i):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        while h >= 1:
            # insert sort
            for i in range(h, n):
                insert_delta(nums, h, i)
            h //= 3
        return nums

    # 快排
    def quick_sort(self, nums, left, right):
        # 小区间可考虑用插入排序
        if right <= left:
            return
        p = self.partition1(nums, left, right)
        self.quick_sort(nums, left, p - 1)
        self.quick_sort(nums, p + 1, right)

    # 基本快排
    def partition1(self, nums, left, right):
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

    # 双指针快排
    def partition2(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]

        pivot = nums[left]  # 基准值
        lt = left + 1
        gt = right
        # 循环不变量
        # all in [left + 1, lt) <= pivot
        # all in (gt, right] >= pivot
        while True:
            while lt <= right and nums[lt] < pivot:
                lt += 1
            while gt > left and nums[gt] > pivot:
                gt -= 1
            if lt >= gt:
                break
            # 相等的元素通过交换，等概率分到数组的两边
            nums[lt], nums[gt] = nums[gt], nums[lt]
            lt += 1
            gt -= 1
        nums[left], nums[gt] = nums[gt], nums[left]
        return gt

    # 三指针快排
    def quick_sort_partition3(self, nums, left, right):
        # 小区间可考虑用插入排序
        if right <= left:
            return
        import random
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]

        # 循环不变量
        # all in [left + 1, lt] < pivot
        # all in [lt + 1, i) = pivot
        # all in [gt, right] > pivot
        pivot = nums[left]
        lt = left
        gt = right + 1

        i = left + 1
        while i < gt:
            if nums[i] < pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
                i += 1
            elif nums[i] == pivot:
                i += 1
            else:
                gt -= 1
                nums[i], nums[gt] = nums[gt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        self.quick_sort_partition3(nums, left, lt - 1)
        self.quick_sort_partition3(nums, gt, right)

    # 堆排序
    def heap_sort(self, nums):
        # 初始化堆(自底向上)
        for i in range(len(nums) - 1, -1, -1):
            self.max_heapify(nums, i, len(nums))
        # 交换元素
        for i in range(len(nums) - 1, -1, -1):
            # 末尾元素与堆顶交换
            nums[i], nums[0] = nums[0], nums[i]
            # 调整堆使剩余元素仍为大根堆
            self.max_heapify(nums, 0, i)

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

    # 归并排序
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    # 桶排序
    def bucket_sort(self, nums):
        # 1 <= nums.length <= 5 * 1e4
        # -5 * 1e4 <= nums[i] <= 5 * 1e4
        OFFSET = int(5e4)
        # step1. 将数据转换为[0, 1e5]
        for i in range(len(nums)):
            nums[i] += OFFSET

        # step2. 设置桶个数
        step_size = 1000
        # num of bucket
        bucket_size = int(1e5 / step_size)

        # step3. 分桶
        bucket = [[] for _ in range(bucket_size + 1)]
        for num in nums:
            bucket_index = int(num // step_size)
            bucket[bucket_index].append(num)

        # step4. 对每个桶插入排序
        for i in range(bucket_size + 1):
            self.insert_sort(bucket[i])

        # step5. 从桶里依次取出
        res = list()
        for i in range(bucket_size + 1):
            if bucket[i]:
                res += [x - OFFSET for x in bucket[i]]
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [5, 1, 1, 0, 0, 2, 50000]
    print(obj.sortArray(nums))