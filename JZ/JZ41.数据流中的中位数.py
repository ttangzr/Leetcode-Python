# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 6:43 PM
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.nums = list()
        self.length = 0

    def Insert(self, num):
        # write code here
        # method-1: insert sort
        self.nums.append(num)
        self.length += 1
        if not self.nums:
            pass
        else:
            tmp = num
            j = self.length - 1
            while j > 0 and self.nums[j - 1] > tmp:
                self.nums[j] = self.nums[j - 1]
                j -= 1
            self.nums[j] = tmp

    def GetMedian(self):
        # write code here
        mid = self.length // 2
        if self.length % 2:
            return self.nums[mid]
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2

if __name__ == '__main__':
    obj = Solution()
    nums = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    for num in nums:
        obj.Insert(num)
        print(obj.GetMedian())
