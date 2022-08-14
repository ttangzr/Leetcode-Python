#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 2:28 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 605-Can Place Flowers.py
# @Software: PyCharm


from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int):
        # method-1: greedy(simple)
        i, bed_len = 0, len(flowerbed)
        while i < bed_len and n > 0:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == bed_len - 1 or flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 3
        return n <= 0
        
        # method-2: greedy
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:    # all zeros before i
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i
        if prev < 0:    # all zeros in flowerbed
            count += (m + 1) // 2
        else:           # the last interval
            count += (m - prev - 1) // 2
        return count >= n

        # method-3: greedy(append zeros)
        count_zero = 1          # zero at the head
        place = 0
        for bed in flowerbed:
            if bed == 0:
                count_zero += 1
            else:
                place += (count_zero - 1) // 2
                if place >= n:
                    return True
                count_zero = 0
        count_zero += 1         # zero at the tail
        place += (count_zero - 1) // 2
        return place >= n


if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    obj = Solution()
    print(obj.canPlaceFlowers(flowerbed, n))
