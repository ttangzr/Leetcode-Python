#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def frequencySort(self, s: str) -> str:
        # method-1: bucket sort
        count = dict()
        for ch in s:
            if count.get(ch) is not None:
                count[ch] += 1
            else:
                count[ch] = 1
        # 根据频次分桶
        bucket = [[] for _ in range(len(s) + 1)]
        for ch, cnt in count.items():
            bucket[cnt].append(ch)
        ret = list()
        for idx in range(len(s) - 1, 0, -1):
            if not bucket[idx]:
                continue
            for ch in bucket[idx]:
                ret += [ch for _ in range(idx)]
        return ''.join(ret)


if __name__ == '__main__':
    obj = Solution()
    s = "tareaea"
    print(obj.frequencySort(s))