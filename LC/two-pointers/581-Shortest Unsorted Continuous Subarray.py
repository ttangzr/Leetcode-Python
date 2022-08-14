# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/7/17 16:15


from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # method-1: two pointer
        n = len(nums)
        maxn, right = float('-inf'), -1
        minn, left = float('inf'), -1
        for i in range(n):
            # find right edge
            if nums[i] >= maxn:
                maxn = nums[i]
            else:
                right = i
            # find left edge
            if nums[n - i - 1] <= minn:
                minn = nums[n - i - 1]
            else:
                left = n - i - 1
        return 0 if right == -1 else right - left + 1


if __name__ == "__main__":
    obj = Solution()
    # nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 2, 3, 3, 3]
    print(obj.findUnsortedSubarray(nums))