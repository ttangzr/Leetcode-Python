# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/9 9:24 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # method-1: sliding window
        occur = set()
        n = len(s)
        r, ans = 0, 0
        for l in range(n):
            if l != 0:
                # 坐指针右移，删除一个字符
                occur.remove(s[l - 1])
            while r <= n - 1 and s[r] not in occur:
                occur.add(s[r])
                r += 1
            # 多移了一个，减掉
            ans = max(ans, r - 1 - l + 1)
        return ans


if __name__ == "__main__":
    obj = Solution()
    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))
