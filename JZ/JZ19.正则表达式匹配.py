# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/28 7:16 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self , str: str, pattern: str):
        # write code here
        # method-1: DP
        m, n = len(str), len(pattern)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                # 判断当j 指向 * 号的时候两种情况：
                if pattern[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if self.match1(str, pattern, i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if self.match1(str, pattern, i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def match1(self, s, p, i, j):
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]


if __name__ == '__main__':
    obj = Solution()
    str, pattern = "aaa","a*a"
    print(obj.match(str, pattern))