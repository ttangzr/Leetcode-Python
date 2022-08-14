# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/8 12:59 PM


from typing import List


class Solution:
    def __init__(self):
        self.index = list()
        self.res = list()

    def countSmaller(self, nums: List[int]):
        # method-1: merge sort
        n = len(nums)
        # 索引数组
        self.index = [i for i in range(n)]
        self.res = [0] * n
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.res

    def merge_sort(self, nums, l, r):
        if l >= r:
             return
        mid = l + (r - l) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid and j <= r:
            # 每次 i 移动一格，就知道右边比 i 位置小的元素个数
            # 取等使得[mid + 1, j)都是小于, 而[i, mid]是小于等于
            if nums[self.index[i]] <= nums[self.index[j]]:
                tmp.append(self.index[i])
                self.res[self.index[i]] += j - (mid + 1)
                i += 1
            else:
                tmp.append(self.index[j])
                j += 1
        while i <= mid:
            tmp.append(self.index[i])
            self.res[self.index[i]] += j - (mid + 1)
            i += 1
        while j <= r:
            tmp.append(self.index[j])
            j += 1
        self.index[l: r + 1] = tmp


if __name__ == "__main__":
    obj = Solution()
    nums = [5, 2, 6, 1]
    print(obj.countSmaller(nums))