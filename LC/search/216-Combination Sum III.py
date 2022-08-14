# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/29 8:40 AM


from typing import List


class Solution:
    def __init__(self):
        self._comb = list()
        self.combinations = list()

    def combinationSum3(self, k: int, n: int):
        # method-1: backtracking
        self.backtracking(1, k, n)
        return self.combinations

    def backtracking(self, start, k, n):
        if n == 0 and k == 0:
            self.combinations.append(list(self._comb))
            return
        for num in range(start, 10):
            if n - num >= 0 and k > 0:
                self._comb.append(num)
                self.backtracking(num + 1, k - 1, n - num)
                self._comb.pop()


if __name__ == '__main__':
    obj = Solution()
    k = 9
    n = 45
    print(obj.combinationSum3(k, n))