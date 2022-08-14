# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 23:36


from typing import List


class UnionFind:
    def __init__(self):
        # 表示26个字母间的连通关系
        self.parent = list(range(26))

    def find(self, index):
        if index == self.parent[index]:
            # parent是本身
            return index
        # 连接
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
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
    equations = ["a==b","b==c","a==c"]
    print(obj.equationsPossible(equations))
