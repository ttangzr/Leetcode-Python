# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/29 8:52 AM


from typing import List


class Solution:
    def __init__(self):
        self.__comb = []
        self.comb = [[]]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            self.backtracking(nums, 0, i + 1)
        return self.comb

    def backtracking(self, nums, start, k):
        if k == 0:
            self.comb.append(list(self.__comb))
            return
        for i in range(start, len(nums)):
            self.__comb.append(nums[i])
            self.backtracking(nums, i + 1, k - 1)
            self.__comb.pop()


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3]
    print(obj.subsets(nums))