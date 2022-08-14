# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/1 15:33

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # method-1: greedy （正向）
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n):
            if max_pos >= i:
                # 更新 max_pos
                max_pos = max(max_pos, i + nums[i])
                # 更新step内能到达的最远pos
                if i == end and i != n - 1:
                    end = max_pos
                    step += 1
        return step


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 3, 1, 1, 4]
    print(obj.jump(nums))