# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/14 3:37 PM


class Solution:
    def minSteps(self, n: int) -> int:
        # method-1: DP
        # j个A复制后粘贴若干次得到i个A，粘贴次数为i//j - 1，加上复制1次为，i//j
        # j是A的因数
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = float("inf")
            j = 1
            # 枚举范围 [1, sqrt(i)]
            while j * j <= i:
                if i % j == 0:
                    f[i] = min(f[i], f[j] + i // j)
                    f[i] = min(f[i], f[i // j] + j)
                j += 1
        return f[n]


if __name__ == '__main__':
    obj = Solution()
    n = 33
    print(obj.minSteps(n))