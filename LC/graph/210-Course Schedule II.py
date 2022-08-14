#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 7:44 下午
# @Author  : T-
# @Site    : 
# @File    : 210-Course Schedule II.py
# @Software: PyCharm

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # method-1: DFS
        edges = defaultdict(list)
        visited = [0] * numCourses
        result = []
        valid = True

        for second, first in prerequisites:
            edges[first].append(second)

        def dfs(course: int):
            nonlocal valid
            visited[course] = 1
            for successor in edges[course]:
                if visited[successor] == 0:
                    dfs(successor)
                elif visited[successor] == 1:
                    valid = False
            visited[course] = 2
            result.append(course)

        for course_idx in range(numCourses):
            if valid and not visited[course_idx]:
                dfs(course_idx)
            elif not valid:
                return []
        return result[::-1]

        # method-2: 拓扑排序
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for second, first in prerequisites:
            edges[first].append(second)
            indeg[second] += 1

        queue = deque([i for i in range(numCourses) if indeg[i] == 0])
        visited = 0
        result = []
        while queue:
            course = queue.popleft()
            visited += 1
            result.append(course)
            for successor in edges[course]:
                indeg[successor] -= 1
                if indeg[successor] == 0:
                    queue.append(successor)
        if visited == numCourses:
            return result
        else:
            return []


if __name__ == "__main__":
    obj = Solution()
    # numCourses = 4
    # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print(obj.findOrder(numCourses, prerequisites))


