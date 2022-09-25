# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/27 17:12

from typing import List
import collections

class UnionFind:
    def __init__(self, n):
        # w[x] = v[x] / v[f_x]
        self.f = list(range(n))     # parents
        self.w = [1.0] * n          # weights

    def find(self, x):
        # w[x] = v[x] / v[father]
        #        w[x] * w[f_x]
        if x != self.f[x]:
            father = self.find(self.f[x])
            self.w[x] = self.w[x] * self.w[self.f[x]]
            self.f[x] = father
        return self.f[x]

    def union(self, x, y, val):
        # w[f_x] =  v[f_x] / v[f_y]
        #           (v[x]/v[y]) * (w[y]/w[x])
        fx, fy = self.find(x), self.find(y)
        self.f[fx] = fy
        self.w[fx] = val * self.w[y] / self.w[x]

    def is_connected(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            return -1.0
        return self.w[x] / self.w[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # method-1: Disjoint-set with weights
        # 1) 给字母编号
        len_equ = len(equations)
        vars = dict()
        nvars = 0
        for i in range(len_equ):
            x, y = equations[i][0], equations[i][1]
            if vars.get(x) is None:
                vars[x] = nvars
                nvars += 1
            if vars.get(y) is None:
                vars[y] = nvars
                nvars += 1
        # 2) union
        uf = UnionFind(nvars)
        for i in range(len_equ):
            x, y = equations[i][0], equations[i][1]
            uf.union(vars[x], vars[y], values[i])
        # 3) 计算
        ans = []
        for q in queries:
            x, y = q[0], q[1]
            if vars.get(x) is None or vars.get(y) is None:
                ans.append(-1.0)
                continue
            ans.append(uf.is_connected(vars[x], vars[y]))
        return ans

        # method-2: DFS
        graph = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v
        def dfs(s, e):
            if s not in graph or e not in graph:
                return -1
            if s == e:
                return 1
            visited.add(s)
            for i in graph[s]:
                if i == e:
                    return graph[s][i]
                if i not in visited:
                    ans = dfs(i, e)
                    if ans != -1:
                        return graph[s][i] * ans
            return -1
        res = []
        for a, b in queries:
            visited = set()
            res.append(dfs(a, b))
        return res


if __name__ == '__main__':
    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    obj = Solution()
    print(obj.calcEquation(equations, values, queries))
