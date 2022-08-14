# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 8:41 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
from typing import List
class Solution:
    def __init__(self):
        self.perm = list()
        self.__perm = list()
        self.__visited = list()

    def Permutation(self , str: str) -> List[str]:
        # write code here
        # method-1: backtracking
        if not str:
            return []
        self.backtracking(0, str)
        return self.perm

    def backtracking(self, start, str):
        if start == len(str):
            res = ''.join(self.__perm)
            if res not in self.perm:
                self.perm.append(res)
            return

        for i in range(len(str)):
            if i not in self.__visited:
                self.__perm.append(str[i])
                self.__visited.append(i)
                self.backtracking(start + 1, str)
                self.__perm.pop()
                self.__visited.pop()


if __name__ == "__main__":
    obj = Solution()
    str =  "aa"
    print(obj.Permutation(str))