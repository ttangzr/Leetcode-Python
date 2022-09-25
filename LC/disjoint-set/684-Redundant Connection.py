#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List

class UnionFind:
    def __init__(self, total):
        self.parent = list(range(total + 1))

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for node1, node2 in edges:
            if uf.find(node1) != uf.find(node2):
                uf.union(node1, node2)
            else:
                return [node1, node2]
        return []

if __name__ == "__main__":
    obj = Solution()
    # edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    edges = [[1,2],[1,3],[2,3]]
    print(obj.findRedundantConnection(edges))

