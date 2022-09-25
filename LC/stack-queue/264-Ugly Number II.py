# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/9/13 11:11

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # method-1: heap
        factors = [2, 3, 5]
        visited = set([1])
        heap = [1]
        # n - 1 ugly numbers
        for _ in range(n - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if cur * factor not in heap:
                    heapq.heappush(heap, cur * factor)
                    visited.add(cur * factor)
        return heapq.heappop(heap)


if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.nthUglyNumber(n))