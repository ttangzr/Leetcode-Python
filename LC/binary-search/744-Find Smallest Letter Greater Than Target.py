#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:19

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # method-1: binary search
        n = len(letters)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l < n else letters[0]

        # letters.extend([chr(ord(x) + 26) for x in letters])
        # n = len(letters)
        # l, r = 0, n - 1
        # ans = idx = 0
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     val = ord(letters[mid])
        #     if val <= ord(target):
        #         l += 1
        #     else:
        #         ans = val
        #         idx = mid
        #         r -= 1
        # return chr(ans) if idx <= (n / 2) - 1 else chr(ans - 26)


if __name__ == '__main__':
    obj = Solution()
    # letters = ["c", "f", "j"]
    # target = "c"    # f
    letters = ["c", "f", "j"]
    target = "j"    # c
    print(obj.nextGreatestLetter(letters, target))








