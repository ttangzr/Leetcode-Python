# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/29 2:20 PM


from typing import List


class Solution:
    def __init__(self):
        self._partition = list()
        self.partitions = list()

    def partition(self, s: str):
        self.backtracking(s)
        return self.partitions

    def backtracking(self, s):
        if len(s) == 0:
            self.partitions.append(list(self._partition))
            return

        for i in range(len(s)):
            if self.isPalidrome(s, 0, i):
                self._partition.append(s[0: i + 1])
                self.backtracking(s[i + 1:])
                self._partition.pop()

    def isPalidrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    obj = Solution()
    s = "aab"
    print(obj.partition(s))