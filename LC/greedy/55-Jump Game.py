# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/15 23:20

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # method-1: greedy
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:  # 当前位置可达
                # 更新能达到的最远距离
                right = max(right, i + nums[i])
                if right >= n - 1:
                    return True
        return False


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 3, 1, 1, 4]
    print(obj.canJump(nums))
