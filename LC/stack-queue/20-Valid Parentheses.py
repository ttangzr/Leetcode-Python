#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # 反括号出栈
                stack.pop()
            else:
                # 正括号入栈
                stack.append(ch)
        # 最后stack必须为空
        return not stack



if __name__ == "__main__":
    obj = Solution()
    str = "()[]({})"
    print(obj.isValid(str))