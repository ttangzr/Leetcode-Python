# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/11 8:37 PM

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # method-1: two points
        # second递增(left->right), third递减(right->left)
        n = len(nums)
        nums.sort()
        res = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # third从right开始
            third = n - 1
            target = - nums[first]
            # second从first + 1开始
            for second in range(first + 1, n):
                # second递增，保证与上一次不同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 保证second<third，寻找target
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 防止second, third指针重叠
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res


if __name__ == "__main__":
    obj = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(obj.threeSum(nums))