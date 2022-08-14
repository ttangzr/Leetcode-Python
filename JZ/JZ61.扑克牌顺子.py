# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/6 10:05 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return bool布尔型
#
from typing import List


class Solution:
    def IsContinuous(self , numbers: List[int]) -> bool:
        # write code here
        # method-1: hash map
        sort_nums = sorted(numbers)
        hashMap = dict()
        _min, _max = 14, 0
        for i in range(len(sort_nums)):
            num = sort_nums[i]
            if num == 0:
                continue
            _min = min(_min, num)
            _max = max(_max, num)
            if hashMap.get(num) is not None:
                return False
            hashMap[num] = 1
        return _max - _min < 5

        # method-2: bit operation
        flag = 0
        _min, _max = 14, 0
        for i in range(len(numbers)):
            num = numbers[i]
            if num == 0:
                continue
            _min = min(_min, num)
            _max = max(_max, num)
            if flag & 1 << num != 0:
                return False
            flag |= 1 << num
        return _max - _min < 5


if __name__ == '__main__':
    obj = Solution()
    numbers = [6, 0, 2, 0, 4]
    print(obj.IsContinuous(numbers))