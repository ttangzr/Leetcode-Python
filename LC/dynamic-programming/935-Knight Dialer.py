#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/15 22:16

class Solution:
    def knightDialer(self, n: int) -> int:
        # method-1: DP
        MOD = 10**9 + 7
        # 对应0-9的映射
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        # start from 1
        dp = [1] * 10
        for i in range(n - 1):
            dp_tmp = [0] * 10
            for num, cnt in enumerate(dp):
                for nex in moves[num]:
                    # 传播至nex
                    dp_tmp[nex] += cnt
                    dp_tmp[nex] %= MOD
            dp = dp_tmp
        return sum(dp) % MOD
                    

if __name__ == '__main__':
    n = 2
    obj = Solution()
    print(obj.knightDialer(n))