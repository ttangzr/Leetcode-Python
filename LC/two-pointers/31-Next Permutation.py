# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/7/17 15:05


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # method-1: two pointers
        n = len(nums)
        if n == 1:
            return
        # 1) find non-decrease num a[i]
        p1 = 0
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
              p1 = i - 1
              break
        # 2) find the first larger num a[j]
        p2 = 0
        for j in range(n - 1, p1, -1):
            if nums[j] > nums[p1]:
                p2 = j
                break
        # 3) swap a[i] and a[j]
        nums[p1], nums[p2] = nums[p2], nums[p1]
        # 4) re-order the nums in [p1+1, n)
        if p1 == p2:
            # reverse case
            nums[:] = nums[::-1]
        else:
            nums[p1 + 1:] = nums[n - 1: p1: -1]



if __name__ == "__main__":
    # nums = [4, 5, 2, 6, 3, 1]
    nums = [3, 2, 1]
    obj = Solution()
    obj.nextPermutation(nums)
    print(nums)