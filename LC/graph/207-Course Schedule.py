#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # method-1: DFS
        # visited: 0: not search, 1: searching, 2: searched
        NOT_SEARCH, SEARCHING, SEARCHED = 0, 1, 2
        visited = [NOT_SEARCH] * numCourses
        edges = defaultdict(list)
        # result = list()       # used in LC210
        for second, first in prerequisites:
            edges[first].append(second)

        def dfs(course):
            visited[course] = SEARCHING
            for next in edges[course]:
                if visited[next] == NOT_SEARCH:
                    if not dfs(next):
                        return False
                elif visited[next] == SEARCHING: # loop
                    return False
            visited[course] = SEARCHED
            # result.append(node)
            return True

        for course_idx in range(numCourses):
            if visited[course_idx] == NOT_SEARCH:
                if not dfs(course_idx):
                    return False
        return True

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
            for next in edges[course]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    queue.append(next)
        return visited == numCourses


if __name__ == "__main__":
    obj = Solution()
    numCourses = 3
    prerequisites = [[0, 1], [2, 0], [1, 2]]
    print(obj.canFinish(numCourses, prerequisites))