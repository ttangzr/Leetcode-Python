'''
Description: 
Author: Zhirong
Date: 2021-05-26 13:07:43
LastEditTime: 2021-05-26 13:45:23
LastEditors: Zhirong
'''

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # method-1: force
        res = ma = 0
        for i, num in enumerate(arr):
            ma = max(num, ma)
            if ma == i:
                res += 1
        return res


if __name__ == "__main__":
    obj = Solution()
    arr = [4,3,2,1,0]
    print(obj.maxChunksToSorted(arr))