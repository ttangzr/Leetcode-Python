# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/20 09:16

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int):
        from collections import Counter
        freq = Counter(tasks)
        # 最多执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量，maxCount
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


if __name__ == "__main__":
    obj = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(obj.leastInterval(tasks, n))