# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 5:07 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
from typing import List


class Solution:
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        # write code here
        # method-1: quick sort
        if k == len(input):
            return input
        return self.quick_sort(input, 0, len(input) - 1, k)

    def quick_sort(self, nums, left, right, k):
        if right <= left:
            return self.quick_sort(nums, 0, len(nums) - 1, k)
        p = self.partition(nums, left, right)
        if p == k:
            return nums[:k]
        elif p > k:
            return self.quick_sort(nums, left, p - 1, k)
        else:
            return self.quick_sort(nums, p + 1, right, k)

    def partition(self, nums, left, right):
        import random
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        lt = left
        # 循环不变量
        # all in [left + 1, lt] < pivot
        # all in [lt + 1, right] >= pivot
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt


if __name__ == '__main__':
    obj = Solution()
    nums, k = [4,5,1,6,2,7,3,8],8
    print(obj.GetLeastNumbers_Solution(nums, k))
