#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # method-1: HashMap
        if not s:
            return 0
        from collections import Counter
        count = Counter(s)
        vals = count.values()
        evens = [i for i in vals if i % 2 == 0]
        odds = [i for i in vals if i % 2 == 1]
        if not odds:
            return sum(evens)
        elif not evens:
            # 减去单独一个的，让odd->even, 再保留一个作为中间的
            return sum(odds) - len(odds) + 1
        else:
            return sum(evens) + sum(odds) - len(odds) + 1

        # method-2: 贪心
        ans = 0
        from collections import Counter
        count = Counter(s)
        for v in count.values():
            # 取偶数个，分别放在两边(3->1)
            ans += v // 2 * 2
            # 此时ans是偶数，且count是比1大的奇数，必定剩下一个放中间
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    s = 'abccccdd'
    print(obj.longestPalindrome(s))
