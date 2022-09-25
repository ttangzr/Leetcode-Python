#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/15 22:02

from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nextday(cells):
            return [int(0 < i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]
        visited = {}
        while n > 0:
            c = tuple(cells)
            if c in visited:
                n %= visited[c] - n
            visited[c] = n
            if n >= 1:
                n -= 1
                cells = nextday(cells)
        return cells
        

if __name__ == '__main__':
    cells = [0,1,0,1,1,0,0,1]
    n = 7
    obj = Solution()
    print(obj.prisonAfterNDays(cells, n))