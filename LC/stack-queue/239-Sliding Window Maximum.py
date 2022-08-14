# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 16:23


from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # method-1: 优先队列/大根堆
        # 每个窗口之间共用k-1个元素
        # 最大值在滑动窗口左边界的左侧
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        import heapq
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

        # method-2: 单调队列
        n = len(nums)
        q = deque()
        # 第一个窗口内单调
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
               q.pop()
            q.append(i)
        # 后续滑动窗口单调
        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans




if __name__ == '__main__':
    obj = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(obj.maxSlidingWindow(nums, k))