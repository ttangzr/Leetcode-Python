# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/10 20:45 PM

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # method-1: moore voting
        res = []
        cand1, cand2 = None, None
        vote1, vote2 = 0, 0
        for num in nums:
            # candidate1 hit
            if vote1 > 0 and num == cand1:
                vote1 += 1
            # candidate2 hit
            elif vote2 > 0 and num == cand2:
                vote2 += 1
            # choose candidate1
            elif vote1 == 0:
                cand1, vote1 = num, 1
            elif vote2 == 0:
                cand2, vote2 = num, 1
            else:
                vote1 -= 1
                vote2 -= 1
        # compute number
        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == cand1:
                cnt1 += 1
            if vote2 > 0 and num == cand2:
                cnt2 += 1
        # validation
        if vote1 > 0 and cnt1 > len(nums) / 3:
            res.append(cand1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            res.append(cand2)
        return res
        

if __name__ == "__main__":
    nums = [1, 2, 2, 3, 2, 3, 1, 1]
    obj = Solution()
    print(obj.majorityElement(nums))