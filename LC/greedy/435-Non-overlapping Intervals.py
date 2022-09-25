#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # method-1: Greedy
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        res = 1
        for i in range(1, len(intervals)):
            # 反之，算最多不重叠的取件
            if intervals[i][0] >= right:
                res += 1
                right = intervals[i][1]
        return len(intervals) - res

        # method-2: DP (timeout)
        if not intervals:
            return 0
        intervals.sort()
        n = len(intervals)
        f = [1]
        for i in range(1, n):
            f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)
        return n - max(f)


if __name__ == "__main__":
    obj = Solution()
    intervals = [ [1,2], [2,3], [3,4], [1,3] ]
    print(obj.eraseOverlapIntervals(intervals))
