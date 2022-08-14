# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/17 9:10 AM


from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # method-1: DP
        # up[i] = max{up[i-1], down[i-1]+1}
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)


if __name__ == '__main__':
    obj = Solution()
    # nums = [1,17,5,10,13,15,10,5,16,8]
    nums = [1, 7, 4, 9, 2, 5]
    print(obj.wiggleMaxLength(nums))