# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/10 9:39 AM


from typing import List


class NumArray:
    def __init__(self,  nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # method-1: DP
        # sumRange(i, j) = sums[j + 1] - sums[i]
        return self.sums[right + 1] - self.sums[left]


if __name__ == '__main__':
    # Your NumArray object will be instantiated and called as such:
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))


