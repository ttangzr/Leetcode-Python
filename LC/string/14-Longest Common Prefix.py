# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/9 9:08 PM

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # method-1: 纵向扫描
        if not strs:
            return ""
        length, cnt = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, cnt):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    obj = Solution()
    print(obj.longestCommonPrefix(strs))