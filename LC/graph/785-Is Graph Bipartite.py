#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # method-1: DFS
        # 未染色节点将其染色未RED，染色节点将相邻节点染为不同的颜色
        # 如果遇到相邻节点被染为相同颜色，说明存在环
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        node_color = [UNCOLORED] * graph_len
        def dfs(node, coloring):
            node_color[node] = coloring
            color_neighbor = GREEN if coloring == RED else RED
            for neighbor in graph[node]:
                if node_color[neighbor] == UNCOLORED:
                    if not dfs(neighbor, color_neighbor):
                        return False
                elif node_color[neighbor] != color_neighbor:
                    return False
            return True
        # 图未必连通，可能存在多个子图
        for idx in range(graph_len):
            if node_color[idx] == UNCOLORED:
                if not dfs(idx, RED):
                    return False
        return True

        # method-2: BFS
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        node_color = [UNCOLORED] * graph_len
        for idx in range(graph_len):
            if node_color[idx] == UNCOLORED:
                stack = deque([idx])
                node_color[idx] = RED
                while stack:        # 层次遍历
                    node = stack.popleft()
                    color_neighbor = GREEN if node_color[node] == RED else RED
                    for neighbor in graph[node]:
                        if node_color[neighbor] == UNCOLORED:
                            stack.append(neighbor)
                            node_color[neighbor] = color_neighbor
                        elif node_color[neighbor] != color_neighbor:
                            return False
        return True


if __name__ == "__main__":
    obj = Solution()
    # graph = [[1,2,3],[0,2],[0,1,3],[0,2]]       # False
    graph = [[1,3],[0,2],[1,3],[0,2]]           # True
    print(obj.isBipartite(graph))

