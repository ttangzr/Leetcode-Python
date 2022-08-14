# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/7/31 11:34 PM

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # method-1: sort
        #       -------
        # odd: [1, 2, 3, 4, 5]
        #             -------
        #
        #        -----------
        # even: [1, 2, 3, 4, 5, 6]
        #              -----------
        # nums.sort()
        # return nums[len(nums) // 2]
    
        # method-2: Moore voting(摩尔投票法)
        # nums:      [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
        # count:      1  2  1  2  1  0   1  0   1  2  1  0   1  2  3  4
        # value:      1  2  1  2  1  0  -1  0  -1 -2 -1  0   1  2  3  4
        # candidate:  7  7  7  7  7  7  5  5  5  5  5  5  7  7  7  7  7
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
            print(count, end="  ")
        return candidate
    

if __name__ == "__main__":
    nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]
    obj = Solution()
    print(obj.majorityElement(nums))