#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # method-1: greedy
        n = len(points)
        if n == 0:
            return 0
        points.sort(key=lambda x: x[1])
        cnt = 1
        right = points[0][1]
        for i in range(1, n):
            if points[i][0] > right:
                cnt += 1
                right = points[i][1]
        return cnt


if __name__ == '__main__':
    obj = Solution()
    # points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # points = [[1, 2]]
    # points = [[1,2], [1,2], [1, 2]]
    # points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(obj.findMinArrowShots(points))

