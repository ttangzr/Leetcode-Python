# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/26 9:26 AM


from typing import List


class Solution:
    def __init__(self):
        self.__perm = []
        self.perm = []
        self.visited = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # sort
        self.visited = [0] * len(nums)
        self.backtracking(nums, 0)
        return self.perm

    def backtracking(self, nums, length):
        if length == len(nums):
            self.perm.append(list(self.__perm))
            return
        for i in range(len(nums)):
            # truncate
            # 对于重复数字，只有visit i-1后才去visit i
            if self.visited[i] == 1 or \
                (i > 0 and nums[i] == nums[i - 1] and self.visited[i - 1] == 0):
                continue
            self.visited[i] = 1
            self.__perm.append(nums[i])
            self.backtracking(nums, length + 1)
            self.__perm.pop()
            self.visited[i] = 0


if __name__ == '__main__':
    nums = [1, 1, 2]
    obj = Solution()
    print(obj.permuteUnique(nums))