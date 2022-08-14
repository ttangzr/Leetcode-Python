# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 5:33 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @param k int整型
# @return int整型
#
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        # method-1: binary search
        # lower bound: first k
        # uppper bound: first element>k
        n = len(data)
        # find lower bound
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid
        lb = l
        # find upper bound
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if data[mid] <= k:
                l = mid + 1
            else:
                r = mid
        ub = l
        return ub - lb