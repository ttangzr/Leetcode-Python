# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/15 12:53 PM


from typing import List


class UnionFind:
    def __init__(self, total):
        self.parent = list(range(total))

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]):
        # method-1: Disjoint-set
        num_provs = len(isConnected)
        uf = UnionFind(num_provs)
        for i in range(num_provs):
            for j in range(i + 1, num_provs):  # pruning
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        circles = sum(uf.parent[i] == i for i in range(num_provs))
        return circles

        # method-2: DFS
        n = len(isConnected)
        ans = list()
        for layer in range(n):
            visited = set()
            visited.add(layer)
            visited = self.dfs(isConnected, layer, visited)
            if visited not in ans:
                ans.append(visited)
        return len(ans)

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