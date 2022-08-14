# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/13 9:37 PM

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # method-1: Binary search
        n = len(nums)
        if target not in nums:
            return -1
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:    # [0, mid]有序
                if nums[0] <= target < nums[mid]:
                    # target在[l, mid - 1]
                    r = mid - 1
                else:
                    # target在[mid + 1, r]
                    l = mid + 1
            else:               # [mid + 1, n - 1]有序
                if nums[mid] < target <= nums[-1]:
                    # target在[mid + 1, r]
                    l = mid + 1
                else:
                    # target在[l, mid - 1]
                    r = mid - 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    nums = [5, 1, 3]
    target = 1
    print(obj.search(nums, target))