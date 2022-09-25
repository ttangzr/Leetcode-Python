#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        ptr_merge = m + n - 1
        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 == -1:
                nums1[ptr_merge] = nums2[ptr2]
                ptr2 -= 1
            elif ptr2 == -1:
                nums1[ptr_merge] = nums1[ptr1]
                ptr1 -= 1
            elif nums1[ptr1] > nums2[ptr2]:
                nums1[ptr_merge] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr_merge] = nums2[ptr2]
                ptr2 -= 1
            ptr_merge -= 1


if __name__ == "__main__":
    obj = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    obj.merge(nums1, m, nums2, n)
    print(nums1)