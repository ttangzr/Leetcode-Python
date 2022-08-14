# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/15 12:53 PM


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]):
        # method-1: DFS
        n = len(isConnected)
        ans = list()
        for layer in range(n):
            visited = set()
            visited.add(layer)
            visited = self.dfs(isConnected, layer, visited)
            if visited not in ans:
                ans.append(visited)
        return len(ans)

        # method-2: Disjoint-set
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1, index2):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))
        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)
        circles = sum(parent[i] == i for i in range(provinces))
        return circles

    def dfs(self, isConnected, layer, visited):
        for idx in range(len(isConnected[layer])):
            if isConnected[layer][idx] == 1 and idx not in visited:
                visited.add(idx)
                self.dfs(isConnected, idx, visited)
        return visited


if __name__ == '__main__':
    obj = Solution()
    isConnected = [[1, 1, 0, 0],
                   [1, 1, 0, 1],
                   [0, 0, 1, 0],
                   [0, 1, 0, 1]]     # 2
    print(obj.findCircleNum(isConnected))