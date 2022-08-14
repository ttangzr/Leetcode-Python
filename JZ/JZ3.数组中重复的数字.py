# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/2 8:33 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
from typing import List

class Solution:
    def duplicate(self , numbers: List[int]):
        # write code here
        # method-1: Hash Map
        hashMap = dict()
        for i, num in enumerate(numbers):
            if hashMap.get(num) is not None:
                return num
            else:
                hashMap[num] = 1
        return -1

        # method-2: sort
        i = 0
        while i < len(numbers):
            if numbers[i] == i:
                i += 1
                continue
            else:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                else:   # swap
                    a, b = numbers[i], numbers[numbers[i]]
                    numbers[i] = b
                    numbers[a] = a
        return -1


if __name__ == "__main__":
    obj = Solution()
    numbers = [2, 3, 1, 0, 2, 5, 3]
    print(obj.duplicate(numbers))