# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/1 4:18 PM


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            l, r = intervals[i]
            start, end = res[-1]
            if l <= end:
                res[-1][1] = max(end, r)
            else:
                res.append([l, r])
        return res


if __name__ == '__main__':
    obj = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]    # [[1,6],[8,10],[15,18]]
    print(obj.merge(intervals))