'''
Description: 
Author: Zhirong
Date: 2021-05-26 08:59:50
LastEditTime: 2021-05-26 09:28:43
LastEditors: Zhirong
'''

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # method-1: poll + visited
        res = 1
        visited = []
        for i in range(len(nums)):
            if nums[i] not in visited:
                checkNum, S = self.check(nums[i], nums)
                visited += S
                res = max(checkNum, res)
        return res



    def check(self, idx, nums):
        cnt = 0
        S = list()
        while idx not in S:
            S.append(idx)
            idx = nums[idx]
            cnt += 1
        return cnt, S
    
        

if __name__ == "__main__":
    obj = Solution()
    nums = [5,4,0,3,1,6,2]
    print(obj.arrayNesting(nums))