# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/27 8:41 AM


from typing import List


class Solution:
    def __init__(self):
        self._comb = list()
        self.combinations = list()

    def combine(self, n: int, k: int) -> List[List[int]]:
        # method-1: backtracking
        self.backtracking(1, k, n)
        return self.combinations

    def backtracking(self, start, k, n):
        if k == 0:
            self.combinations.append(list(self._comb))
            return
        for i in range(start, n - k + 2):   # pruning: start->n-k+1
            self._comb.append(i)
            self.backtracking(i + 1, k - 1, n)
            self._comb.pop()


if __name__ == '__main__':
    obj = Solution()
    n = 4
    k = 2
    print(obj.combine(n, k))