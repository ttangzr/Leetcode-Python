#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/14 23:35

class MedianFinder:
    def __init__(self):
        self.queMax = []    # 小根堆，取出大于中位数的
        self.queMin = []    # 转换为大根堆，取出小于中位数的

    def addNum(self, num: int) -> None:
        if not self.queMin or num <= -self.queMin[0]:
            heapq.heappush(self.queMin, -num)
            if len(self.queMax) + 1 < len(self.queMin):
                heapq.heappush(self.queMax, -heapq.heappop(self.queMin))
        else:
            heapq.heappush(self.queMax, num)
            if len(self.queMax) > len(self.queMin):
                heapq.heappush(self.queMin, -heapq.heappop(self.queMax))

    def findMedian(self) -> float:
        if len(self.queMin) > len(self.queMax):
            return -self.queMin[0]
        return (-self.queMin[0] + self.queMax[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()