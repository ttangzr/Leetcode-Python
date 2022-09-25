# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/17 9:10 AM


from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # method-1: DP
        # up:
        # nums[i] > nums[i-1]: up[i] = max{up[i-1], down[i-1]+1}
        # nums[i] <=nums[i-1]: up[i] = up[i-1]
        # down
        # nums[i] < nuns[i-1]: down[i] = max{down[i-1], up[i-1]+1}
        # nums[i] >=nums[i-1]: down[i] = down[i-1]
        n = len(nums)
        if n < 2:
            return n
        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = max(down[i - 1], up[i - 1] + 1)
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[n - 1], down[n - 1])
        
        # method-2: DP (optimized)
        # up和down的绝对值之差不超过1
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # up = max(up, down + 1)
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # down = max(down, up + 1)
                down = up + 1
        return max(up, down)
    
        # method-3: greedy
        n = len(nums)
        if n < 2:
            return n
        prevdiff = nums[1] - nums[0]
        ret = 2 if prevdiff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
        return ret
        

if __name__ == '__main__':
    obj = Solution()
    # nums = [1,17,5,10,13,15,10,5,16,8]
    # nums = [1, 7, 4, 9, 2, 5]
    nums = [3,3,3,2,5]
    print(obj.wiggleMaxLength(nums))