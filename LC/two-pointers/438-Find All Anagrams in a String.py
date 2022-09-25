# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/21 20:25

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # method-1: sliding window
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        s_count = [0] * 26
        p_count = [0] * 26
        a = ord('a')
        for i in range(p_len):
            s_count[ord(s[i]) - a] += 1
            p_count[ord(p[i]) - a] += 1
        ans = []
        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - a] -= 1
            # 尾部+1
            s_count[ord(s[i + p_len]) - a] += 1
            if s_count == p_count:
                ans.append(i + 1)
        return ans


if __name__ == "__main__":
    obj = Solution()
    # s = "cbaebabacd"
    # p = "abc"
    s = "abab"
    p = "ab"
    print(obj.findAnagrams(s, p))
    