#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest = ""
        for target in dictionary:
            len_longest, len_target = len(longest), len(target)
            if len_longest > len_target or \
                    (len_longest == len_target and longest < target):
                continue
            if self.isSubstr(s, target):
                longest = target
        return longest

    def isSubstr(self, s: str, target: str) -> bool:
        p_s, p_target = 0, 0
        while p_s < len(s) and p_target < len(target):
            if s[p_s] == target[p_target]:
                p_target += 1
            p_s += 1
        return p_target == len(target)


if __name__ == "__main__":
    obj = Solution()
    s = "bab"
    dictionary = ["ba", "ab", "a", "b"]
    # s = "abpcplea"
    # dictionary = ["ale", "apple", "monkey", "plea"]
    # s = "abpcplea"
    # dictionary = ["ale", "apple", "monkey", "plea",
    #               "abpcplaaa", "abpcllllll", "abccclllpppeeaaaa"]
    print(obj.findLongestWord(s, dictionary))