# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/08 09:27 PM

class Solution:
    def numTrees(self, n: int) -> int:
        # method-1: DP
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for nn in range(2, n + 1):
            for i in range(1, nn + 1):
                G[nn] += G[i - 1] * G[nn - i]
        return G[n]

