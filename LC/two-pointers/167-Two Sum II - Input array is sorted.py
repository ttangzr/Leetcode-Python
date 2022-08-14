#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 8:23 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 167-Two Sum II - Input array is sorted.py
# @Software: PyCharm

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return []



if __name__ == "__main__":
    obj = Solution()
    numbers = [2, 3, 4]
    target = 6
    print(obj.twoSum(numbers, target))
