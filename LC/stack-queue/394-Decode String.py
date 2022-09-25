# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/7 21:50


class Solution:
    def decodeString(self, s: str) -> str:
        # method-1: stack
        stack = []
        ptr = 0
        while ptr < len(s):
            ch = s[ptr]
            if ch.isdigit():
                # 获取字符串前数字进栈
                stack.append(ch)
                ptr += 1
            elif ch.isalpha() or ch == '[':
                # 获取字母进栈
                stack.append(ch)
                ptr += 1
            else:
                # ch == ']'
                # 子栈保存string
                sub_stk = []
                while stack[-1] != '[':
                    sub_stk.append(stack.pop())
                sub_stk = sub_stk[::-1]
                strings = ''.join(sub_stk)
                # '[' 出栈
                stack.pop()
                # digits出栈
                sub_stk = []
                while stack and stack[-1].isdigit():
                    sub_stk.append(str(stack.pop()))
                sub_stk = sub_stk[::-1]
                digits = int(''.join(sub_stk))
                # decode string入栈
                for _ in range(digits):
                    stack.append(strings)
                ptr += 1
        return ''.join(stack)



if __name__ == '__main__':
    obj = Solution()
    s = "abc3[a2[c]]xyz"
    # s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(obj.decodeString(s))