# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/16 8:59 AM


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # method-1: DP
        # dp[i]是前i个元素以第i个元素结尾的最长上升序列长度
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # method-2: 贪心+二分查找
        d = []
        for num in nums:
            if not d or num > d[-1]:
                # 如果大于d最后一个元素，就append进去
                d.append(num)
            else:
                # 否则在d中寻找较小的并替换
                l, r = 0, len(d) - 1
                # 替换的位置
                loc = r
                while l <= r:
                    mid = (l + r) >> 1
                    if d[mid] >= num:
                        r = mid - 1
                        loc = mid
                    else:
                        l = mid + 1
                # 替换
                d[loc] = num
        return len(d)


if __name__ == '__main__':
    obj = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [7, 7, 7, 7]
    # nums = [4, 10, 4, 3]
    # nums = [10,9,2,5,3,7,101,18]
    print(obj.lengthOfLIS(nums))