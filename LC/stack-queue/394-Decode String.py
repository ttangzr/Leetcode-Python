# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/7 21:50


class Solution:
    def decodeString(self, s: str) -> str:
        # method-1: stack
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # decoding result
                content = []
                while stack and stack[-1] != '[':
                    content.append(stack.pop())
                content = content[::-1]     # remember reverse
                stack.pop()                 # pop '['
                # decoding k
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num = num[::-1]             # remember reverse
                # combine
                decoded = int(''.join(num)) * ''.join(content)
                # append to stack
                stack += list(decoded)
        return ''.join(stack)


if __name__ == '__main__':
    obj = Solution()
    # s = "abc3[a2[c]]xyz"
    s = "10[abc]"
    print(obj.decodeString(s))