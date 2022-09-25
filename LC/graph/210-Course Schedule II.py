#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # method-1: DFS
        NOT_SEARCH, SEARCHING, SEARCHED = 0, 1, 2
        edges = defaultdict(list)
        visited = [NOT_SEARCH] * numCourses
        result = []

        for second, first in prerequisites:
            edges[first].append(second)

        def dfs(course):
            visited[course] = SEARCHING
            for next in edges[course]:
                if visited[next] == NOT_SEARCH:
                    if not dfs(next):
                        return False
                elif visited[next] == SEARCHING:
                    return False
            visited[course] = SEARCHED
            result.append(course)
            return True

        for course_idx in range(numCourses):
            if visited[course_idx] == NOT_SEARCH:
                if not dfs(course_idx):
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
            for next in edges[course]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    queue.append(next)
        return result if visited == numCourses else []


if __name__ == "__main__":
    obj = Solution()
    # numCourses = 4
    # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print(obj.findOrder(numCourses, prerequisites))


