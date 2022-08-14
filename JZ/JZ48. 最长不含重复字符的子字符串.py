# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 12:32 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def lengthOfLongestSubstring(self , s: str) -> int:
        # write code here
        # method-1: DP
        hashMap = dict()
        start, sub_len = -1, 1
        for i in range(len(s)):
            if hashMap.get(s[i]) is not None:
                start = max(start, hashMap[s[i]])
            hashMap[s[i]] = i
            sub_len = max(sub_len, i - start)
        return sub_len


if __name__ == '__main__':
    obj = Solution()
    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))
