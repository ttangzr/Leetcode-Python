# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/28 8:47 AM


from typing import List


class Solution:
    def __init__(self):
        self._comb = list()
        self.combinations = list()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target)
        return self.combinations

    def backtracking(self, candidates, target):
        if target == 0:
            self.combinations.append(list(self._comb))
            return

        for idx in range(len(candidates)):
            num = candidates[idx]
            if target - num >= 0:
                self._comb.append(num)
                self.backtracking(candidates[idx:], target - num)
                self._comb.pop()

if __name__ == '__main__':
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(obj.combinationSum(candidates, target))