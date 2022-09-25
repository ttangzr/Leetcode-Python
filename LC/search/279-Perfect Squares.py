# -*- coding: utf-8 -*-
# @Author  : ZhirongTang
# @Time    : 2021/12/8 2:59 PM


class Solution:
    def numSquares(self, n: int) -> int:
        # method-1: BFS
        # squares是search spaces
        #      8
        #     / \
        #    7   4
        #   / \
        #  6   3
        # ...
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        visited = set()
        queue = [n]
        level = 1
        while queue:
            for _ in range(len(queue)):     # 层次遍历
                curr = queue.pop(0)
                for s in squares:
                    next = curr - s
                    if next == 0:
                        return level
                    elif next > 0 and next not in visited:
                        queue.append(next)
                        visited.add(next)
            level += 1
        return -1

        # method-2: DP
        # x + j * j = i
        # dp[x] + 1 = dp[i]
        # dp[i] = min{dp[i], dp[i - j * j] + 1}
        # 范围[1, sqrt(i)]
        import math
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i  # bad case: all 1
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


if __name__ == '__main__':
    obj = Solution()
    n = 8
    print(obj.numSquares(n))