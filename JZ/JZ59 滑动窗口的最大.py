# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 5:26 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self , num: List[int], size: int) -> List[int]:
        # write code here
        n = len(num)
        ret = list()
        if size > n or size == 0:
            return []
        for i in range(0, n - size + 1):
            ret.append(max(num[i: i + size]))
        return ret