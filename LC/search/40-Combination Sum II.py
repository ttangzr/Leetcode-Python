# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/28 5:03 PM


from typing import List


class Solution:
    def __init__(self):
        self.__comb = []
        self.comb = []
        self.visited = []
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.visited = [0] * len(candidates)
        self.backtracking(candidates, target, 0)
        return self.comb

    def backtracking(self, candidates, target, start):
        if target == 0:
            self.comb.append(list(self.__comb))
            return
        for i in range(start, len(candidates)):
            if self.visited[i] == 1 or \
                (i != 0 and candidates[i] == candidates[i - 1] and self.visited[i - 1] == 0):
                continue
            if target - candidates[i] >= 0:
                self.__comb.append(candidates[i])
                self.visited[i] = 1
                self.backtracking(candidates, target - candidates[i], i + 1)
                self.__comb.pop()
                self.visited[i] = 0


if __name__ == '__main__':
    obj = Solution()
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # target = 8
    candidates = [2, 5, 2, 1, 2]
    target = 5
    # candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # target = 27
    print(obj.combinationSum2(candidates, target))

