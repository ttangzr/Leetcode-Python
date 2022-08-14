# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/8 9:55 AM


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # method-1: DP(opt)
        # 完全背包问题，存在问题，涉及放入顺序，物品放最内存循环
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            for word in wordDict:
                word_len = len(word)
                if j >= word_len and word == s[j - word_len: j]:
                    dp[j] = dp[j] | dp[j - word_len]
        return dp[n]


if __name__ == '__main__':
    obj = Solution()
    s = "applepenapple"
    ordDict = ["apple", "pen"]
    print(obj.wordBreak(s, ordDict))