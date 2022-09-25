#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # method-1: bit operation
        len_words = len(words)
        # 26个字母对应26位bit
        words_bit = [0] * len_words
        for i in range(len_words):
            for ch in words[i]:
                words_bit[i] |= 1 << (ord(ch) - ord('a'))
        res = 0
        for i in range(len_words):
            # pruning
            for j in range(i + 1, len(words_bit)):
                if words_bit[i] & words_bit[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res


if __name__ == "__main__":
    obj = Solution()
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(obj.maxProduct(words))