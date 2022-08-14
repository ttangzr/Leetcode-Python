# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/7 23:05


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        ans = ""
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry != 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            res = n1 + n2 + carry
            ans += str(res % 10)
            carry = res // 10
            p1 -= 1
            p2 -= 1
        return ans[::-1]


if __name__ == "__main__":
    obj = Solution()
    num1 = "1456"
    num2 = "77"
    print(obj.addStrings(num1, num2))
