# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 8:13 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param rotateArray int整型一维数组
# @return int整型
#
from typing import List
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        # method-1: binary search
        l, r = 0, len(rotateArray) - 1
        while l < r:
            mid = l + (r - l) // 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            elif rotateArray[mid] < rotateArray[r]:
                r = mid
            else:   # mid == target
                r -= 1
        return rotateArray[l]

if __name__ == '__main__':
    obj = Solution()
    # rotateArray = [3, 4, 5, 1, 2]
    rotateArray = [1,0,1,1,1]
    print(obj.minNumberInRotateArray(rotateArray))
