# -*- coding: utf-8 -*-
# @Author  : ZhirongTang
# @Time    : 2021/12/7 10:36 AM


from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # method-1: BFS
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        elif n <= 2:
            return n
        queue = [(0, 0, 1)]
        grid[0][0] = 1  # visited
        while queue:
            i, j, step = queue.pop(0)
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (1, -1), (1, 1)]:
                if i + dx == n - 1 and j + dy == n - 1:
                    return step + 1
                if 0 <= i + dx < n and 0 <= j +  dy < n and grid[i + dx][j + dy] == 0:
                    queue.append((i + dx, j + dy, step + 1))
                    grid[i + dx][j + dy] = 1    # visited
        return - 1

        # method-2: A* search
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        elif n <= 2:
            return n

        def heuristic(x, y):
            return max(abs(n - 1 - x), abs(n - 1 - y))

        h = []
        import heapq
        heapq.heappush(h, (0, (0, 0, 1)))
        visited = []
        while h:
            _, (i, j, step) = heapq.heappop(h)
            if [i, j] in visited:
                continue
            visited.append([i, j])
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (1, -1), (1, 1)]:
                next_i = i + dx
                next_j = j + dy
                if next_i == n - 1 and next_j == n - 1:
                    return step + 1
                if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0:
                    heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step + 1)))
        return -1

if __name__ == '__main__':
    obj = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(obj.shortestPathBinaryMatrix(grid))