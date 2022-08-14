# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/22 18:58


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # method-1: DP
        # f[i][j]
        # 表示s前i个字符与p前j个字符能否匹配
        # 1) j为字母，f[i][j] = f[i-1][j-1] if s[i]=p[j]
        # 2) j为*,   f[i][j] = f[i-1][j]|f[i][j-1] 使用/不使用*
        # 3) j为?，  f[i][j] = f[i-1][j-1]
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        # f[i][0] = False
        # f[0][j], p[j]=*: True, else: False
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                f[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] = f[i - 1][j - 1] | f[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
        return f[m][n]


if __name__ == '__main__':
    obj = Solution()
    s = "acdcb"
    p = "a*c?b"
    print(obj.isMatch(s, p))
