#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def partitionLabels(self, s: str):
        # method-1:greedy
        hashMap = dict()
        size = len(s)
        # 记录每个字母第一次和最后一次出现的索引
        for i in range(size):
            if hashMap.get(s[i]) is not None: # update last time appear
                hashMap[s[i]][1] = i
            else:   # first time appear
                hashMap[s[i]] = [i, i]

        partition = list()
        left = -1
        right = -1
        for ch in s:
            start, end = hashMap[ch]
            if start > left and end < right:
                # 包含
                continue
            elif start > left and start < right and end > right:
                # 重叠，更新右端点
                right = end
                partition[-1] = right - left + 1
            elif start > right:
                # 无重叠，更新左右端点
                left = start
                right = end
                partition.append(right - left + 1)
        return partition


if __name__ == "__main__":
    obj = Solution()
    S = "ababcbacadefegdehijhklij"  # [9, 7, 8]
    print(obj.partitionLabels(S))
