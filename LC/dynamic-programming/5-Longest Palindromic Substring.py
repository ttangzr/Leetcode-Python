# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 17:08


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # method-1: DP
        n = len(s)
        if n < 2:
            return s
        # record palindrome result
        begin, max_len = 0, 1
        # dp[i][j]: s[i...j] is palindrome
        dp = [[False] * n for _ in range(n)]
        # boundary1: sz=1
        for i in range(n):
            dp[i][i] = True
        # 枚举不同长度
        for sz in range(2, n + 1):
            # 枚举不同的起始位置
            for j in range(sz - 1, n):
                # j - i + 1 = sz
                i = j - sz + 1
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # s[i] == s[j]
                    # boundary2: sz=2
                    # j - 1 - (i + 1) + 1 < 2
                    # -> j - 3 < 3
                    if (j - 1) - (i + 1) + 1 < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # update max_len
                if dp[i][j] and sz > max_len:
                    begin, max_len = i, sz
        return s[begin: begin + max_len]
        
        # method-2:中心拓展
        start, end = 0, 0
        for i in range(len(s)):
            # 奇数
            s1, e1 = self.extendSubstrings(s, i, i)
            # 偶数
            s2, e2 = self.extendSubstrings(s, i, i + 1)
            if e1 - s1 > end - start:
                start, end = s1, e1
            if e2 - s2 > end - start:
                start, end = s2, e2
        return s[start: end + 1]

    def extendSubstrings(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end - 1


if __name__ == '__main__':
    obj = Solution()
    s = "babad"
    print(obj.longestPalindrome(s))