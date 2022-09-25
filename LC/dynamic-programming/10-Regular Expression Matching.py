# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/22 19:01


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # method-1: DP
        # f[i][j]表示s前i个字符与p前j个字符能否匹配
        # 1) j为字母，f[i][j] = f[i-1][j-1] if s[i]=p[j]
        # 2) j为*,   f[i][j] = f[i-1][j]|f[i][j-2] if s[i]=p[j-1] (丢掉一个字符继续匹配）
        #                   =  f[i][j-2]           if s[i]!=p[j-1]
        # 3) j为.，  f[i][j] = f[i-1][j-1]
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 不匹配该字符，对j-2个字符匹配任意次
                    f[i][j] |= f[i][j - 2]
                    # 匹配s末尾的一个字符
                    if self.match(s, p, i, j -1):
                        f[i][j] |= f[i - 1][j]
                else:
                    # 必须在s中匹配一个字母
                    if self.match(s, p, i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def match(self, s, p, i, j):
        # Note: input i, j must -1
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]


if __name__ == '__main__':
    obj = Solution()
    s = "aa"
    p = "a*"
    print(obj.isMatch(s, p))
