# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/21 9:06 AM


from typing import List


class Solution:
    def __init__(self):
        self.phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        self.combinations = list()
        self._comb = list()

    def letterCombinations(self, digits: str) -> List[str]:
        # method-1: backtracking
        if not len(digits):
            return []
        self.backtracking(digits, 0)
        return self.combinations

    def backtracking(self, digits, index):
        if index == len(digits):
            self.combinations.append("".join(self._comb))
        else:
            digit = digits[index]
            for letter in self.phoneMap[digit]:
                self._comb.append(letter)
                self.backtracking(digits, index + 1)
                self._comb.pop()


if __name__ == '__main__':
    digits = "23"
    obj = Solution()
    print(obj.letterCombinations(digits))

