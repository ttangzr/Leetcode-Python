# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/2 8:20 PM


from typing import List

class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums: List[int]) -> int:
        # write code here
        # method-1: merge sort
        if len(nums) <= 1:
            return 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.count

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
                # [i, mid]皆为逆序对
                self.count += mid + 1 - i
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp


if __name__ == '__main__':
    obj = Solution()
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    print(obj.reversePairs(data))