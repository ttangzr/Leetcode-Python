# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 7:51 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
from typing import List
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        # method-1: binary search
        m, n = len(array), len(array[0])
        if m == 0 or n == 0:
            return False
        row, col = 0, n - 1
        while row < m and col >= 0:
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row += 1
            else:
                col -= 1
        return False


if __name__ == "__main__":
    obj = Solution()
    target, array = 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(obj.Find(target, array))