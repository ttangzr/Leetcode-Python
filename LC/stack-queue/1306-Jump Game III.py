# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 16:07


from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # method-1: queue + BFS
        if arr[start] == 0:
            return True
        n = len(arr)
        visited = set([start])
        que = deque([start])
        while que:
            cur = que.popleft()
            for nex in [cur - arr[cur], cur + arr[cur]]:
                if 0 <= nex < n and nex not in visited:
                    if arr[nex] == 0:
                        return True
                    visited.add(nex)
                    que.append(nex)
        return False


if __name__ == "__main__":
    obj = Solution()
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(obj.canReach(arr, start))