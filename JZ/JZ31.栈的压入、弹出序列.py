# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 12:37 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self , pushV: List[int], popV: List[int]) -> bool:
        # write code here
        n = len(pushV)
        stack = list()
        i, j = 0, 0
        while i < n:
            stack.append(pushV[i])
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
            i += 1
        return j == n