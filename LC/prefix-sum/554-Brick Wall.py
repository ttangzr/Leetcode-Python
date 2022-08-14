# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 15:10


from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # method-1: prefix sum
        brick_levels = len(wall)
        prefix_sum = defaultdict(int)
        for i in range(len(wall)):
            curr_sum = 0
            # 计算每一层缝隙的prefix sum,最后一个brick不算
            for j in range(len(wall[i]) - 1):
                curr_sum += wall[i][j]
                prefix_sum[curr_sum] += 1
        # 穿过的brick即为level减去缝隙数
        return brick_levels - max(prefix_sum.values(), default=0)


if __name__ == "__main__":
    obj = Solution()
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    # wall = [[1], [1], [1]]
    # wall = [[1,1],[2],[1,1]]
    # wall = [[100000000],[100000000],[100000000]]
    print(obj.leastBricks(wall))