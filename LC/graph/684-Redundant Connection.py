#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/8 9:35 上午
# @Author  : T-
# @Site    : 
# @File    : 684-Redundant Connection.py
# @Software: PyCharm

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        def find(index: int):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []        


if __name__ == "__main__":
    obj = Solution()
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(obj.findRedundantConnection(edges))

