# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/6 10:48 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def StrToInt(self , s: str) -> int:
        # write code here
        start = False
        negative = False
        nums = list()
        for i in range(len(s)):
            if not start:
                if s[i] == ' ':
                    pass
                elif s[i] == '+':
                    start = True
                elif s[i] == '-':
                    start = True
                    negative = True
                elif ord('0') <= ord(s[i]) <= ord('9'):
                    start = True
                    nums.append(s[i])
                else:
                    return 0
                continue
            else:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    nums.append(s[i])
                else:
                    break
        if not nums:
            return 0
        num = int(''.join(nums))
        num = - num if negative else num
        num = 0x7fffffff if num >= 0x7fffffff else num
        num = -0x80000000 if num <= -0x80000000 else num
        return num


if __name__ == "__main__":
    obj = Solution()
    s = ""
    print(obj.StrToInt(s))
