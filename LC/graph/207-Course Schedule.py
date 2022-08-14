#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 6:37 下午
# @Author  : T-
# @Site    : 
# @File    : 207-Course Schedule.py
# @Software: PyCharm


from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # method-1: DFS
        # visited: 0: not search, 1: searching, 2: searched
        edges = defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for second, first in prerequisites:
            edges[first].append(second)

        def dfs(node):
            nonlocal valid
            visited[node] = 1
            for idx in edges[node]:
                if visited[idx] == 0:
                    dfs(idx)
                    if not valid:
                        return
                elif visited[idx] == 1:
                    valid = False
            visited[node] = 2
            result.append(node)

        for course_idx in range(numCourses):
            if valid and not visited[course_idx]:
                dfs(course_idx)
        return valid


        # method-2: BFS (拓扑排序)
        # 想要修课程0，必须先完成课程1->课程1的后继节点为课程0
        # 邻接表：每个节点的后继节点
        edges = defaultdict(list)
        # 入度：指向这个节点的节点个数
        indeg = [0] * numCourses
        # step1: 建立邻接表和入度
        for second, first in prerequisites:
            edges[first].append(second)
            indeg[second] += 1
        # step2: 拓扑排序前，先把所有入度为0的节点加入队列，从这些节点开始搜索
        queue = deque([i for i in range(numCourses) if indeg[i] == 0])
        visited = 0
        while queue:
            visited += 1
            course = queue.popleft()
            # step3: 把该节点的后继节点入度-1，如果入度为0，就加入队列
            for successor in edges[course]:
                indeg[successor] -= 1
                if indeg[successor] == 0:
                    queue.append(successor)
        return visited == numCourses


if __name__ == "__main__":
    obj = Solution()
    numCourses = 3
    prerequisites = [[0, 1], [2, 0], [1, 2]]
    print(obj.canFinish(numCourses, prerequisites))