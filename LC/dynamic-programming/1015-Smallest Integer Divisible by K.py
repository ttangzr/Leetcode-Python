# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/19 22:26

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # method-1: 计数类模拟
        # 后缀一定不能为024568
        if k % 2 == 0 or k % 5 == 0:
            return -1
        num = 1
        cnt = 1
        while num % k != 0:
            num = (num * 10 + 1) % k
            cnt += 1
        return cnt


if __name__ == '__main__':
    obj = Solution()
    k = 3
    print(obj.smallestRepunitDivByK(k))
