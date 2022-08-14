# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/17 8:58 AM


from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # method-1: DP
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    obj = Solution()
    # pairs = [[1,2], [2,3], [3,4], [5,6]]
    pairs = [[1,2],[7,8],[4,5]]
    print(obj.findLongestChain(pairs))