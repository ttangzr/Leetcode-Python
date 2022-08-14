# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 16:07


from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        visited = {start}
        q = deque([start])
        while q:
            idx = q.popleft()
            for i in [idx - arr[idx], idx + arr[idx]]:
                if 0 <= i < n and i not in visited:
                    if arr[i] == 0:
                        return True
                    visited.add(i)
                    q.append(i)
        return False


if __name__ == "__main__":
    obj = Solution()
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(obj.canReach(arr, start))