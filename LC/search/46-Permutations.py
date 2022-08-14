# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/26 8:50 AM


from typing import List


class Solution:
    def __init__(self):
        self.__perm = []
        self.perm = []
        self.visited = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # method-1: backtracking
        self.visited = [0] * len(nums)
        self.backtracking(nums, 0)
        return self.perm

    def backtracking(self, nums, length):
        if length == len(nums):
            self.perm.append(list(self.__perm))
            return 
        for i in range(len(nums)):
            if self.visited[i] == 1:
                continue
            self.visited[i] = 1
            self.__perm.append(nums[i])
            self.backtracking(nums, length + 1)
            self.visited[i] = 0
            self.__perm.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution()
    print(obj.permute(nums))
