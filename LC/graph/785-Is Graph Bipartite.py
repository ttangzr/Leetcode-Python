#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 8:16 下午
# @Author  : T-
# @Site    :
# @File    : 785-Is Graph Bipartite.py
# @Software: PyCharm

from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 未染色节点将其染色未RED，染色节点将相邻节点染为不同的颜色
        # 如果遇到相邻节点被染为相同颜色，说明存在环
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * graph_len
        valid = True

        # method-1: DFS
        def dfs(node, coloring):
            nonlocal valid
            color[node] = coloring
            color_neighbor = GREEN if coloring == RED else RED
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, color_neighbor)
                    if not valid:
                        return
                elif color[neighbor] != color_neighbor:
                    valid = False
                    return
        for idx in range(graph_len):
            if color[idx] == UNCOLORED:
                dfs(idx, RED)
                if not valid:
                    break
        return valid

        # method-2: BFS
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * graph_len
        for idx in range(graph_len):
            if color[idx] == UNCOLORED:
                stack = deque([idx])
                color[idx] = RED
                while stack:
                    node = stack.pop()
                    color_neighbor = GREEN if color[node] == RED else RED
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            stack.append(neighbor)
                            color[neighbor] = color_neighbor
                        elif color[neighbor] != color_neighbor:
                            return False


if __name__ == "__main__":
    obj = Solution()
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]       # False
    # graph = [[1,3],[0,2],[1,3],[0,2]]           # True
    print(obj.isBipartite(graph))

