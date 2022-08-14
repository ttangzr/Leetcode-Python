# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 8:35 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        # write code here
        # method-1: bit operation
        # 全部数的异或结果
        xor = 0
        for arr in array:
            xor ^= arr
        # 得到最低位的1作为mask
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        # 对mask为0/1进行分组
        a, b = 0, 0
        for arr in array:
            if arr & mask:
                a ^= arr
            else:
                b ^= arr
        return [a, b] if a < b else [b, a]


if __name__ == "__main__":
    obj = Solution()
    array = [1, 2, 3, 3, 2, 9]
    print(obj.FindNumsAppearOnce(array))