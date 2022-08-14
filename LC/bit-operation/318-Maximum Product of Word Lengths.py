#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 8:51 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 318-Maximum Product of Word Lengths.py
# @Software: PyCharm


from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # method-1: 位操作+预计算+HashMap
        words_len = len(words)
        val = [0] * words_len
        for string_idx in range(words_len):
            for ch in words[string_idx]:
                # 每个字母映射到一个bit
                val[string_idx] |= 1 << (ord(ch) - ord('a'))

        ret = 0
        for i in range(words_len):
            # 剪枝
            for j in range(i+1, words_len):
                if val[i] & val[j] == 0:
                    # AND=0说明没有交集
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret


if __name__ == "__main__":
    obj = Solution()
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(obj.maxProduct(words))