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
                max_cnt, arr = self.search(nums[i], nums)
                visited += arr
                res = max(max_cnt, res)
        return res

    def search(self, i, nums):
        max_cnt, res = 0, []
        while i not in res:
            res.append(i)
            i = nums[i]
            max_cnt += 1
        return max_cnt, res
        

if __name__ == "__main__":
    obj = Solution()
    nums = [5,4,0,3,1,6,2]
    print(obj.arrayNesting(nums))