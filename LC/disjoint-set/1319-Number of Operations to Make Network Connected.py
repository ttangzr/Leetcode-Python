# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/27 16:49

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # method-1: Disjoint-set
        redundants = 0
        uf = UnionFind(n)
        for con in connections:
            pc1, pc2 = con[0], con[1]
            if uf.find(pc1) != uf.find(pc2):
                uf.union(pc1, pc2)
            else:
                # 冗余连接
                redundants += 1
        # 总网络数
        netwks = sum(uf.parent[i] == i for i in range(n))
        if redundants >= netwks - 1:
            return netwks - 1
        else:
            return -1


if __name__ == "__main__":
    obj = Solution()
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    # n = 6
    # connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
    # n = 5
    # connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
    print(obj.makeConnected(n, connections))