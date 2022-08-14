# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/27 2:58 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
from typing import List
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
        # write code here
        # method-1: DP(optimized)
        dp = 0
        max_val = array[0]
        start, end = 0, 0
        m_start, m_end = 0, 0
        for i in range(len(array)):
            if array[i] > dp + array[i]:
                start, end = i, i
                dp = array[i]
            else:
                dp = dp + array[i]
                end = i
            if dp >= max_val:
                max_val = dp
                m_start, m_end = start, end
        return array[m_start: m_end + 1]


if __name__ == "__main__":
    obj = Solution()
    # array = [1, -2, 3, 10, -4, 7, 2, -5]
    array = [1,2,-3,4,-1,1,-3,2]
    print(obj.FindGreatestSumOfSubArray(array))
