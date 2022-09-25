# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 23:36

from typing import List

class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, index):
        if index != self.parent[index]:
            # index is not parent, find index's parent
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        # union index1's and index2 's parents
        self.parent[self.find(index1)] = self.find(index2)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                uf.union(index1, index2)
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                if uf.find(index1) == uf.find(index2):
                    return False
        return True


if __name__ == '__main__':
    obj = Solution()
    equations = ["a==b","b!=c","a==c"]
    print(obj.equationsPossible(equations))
