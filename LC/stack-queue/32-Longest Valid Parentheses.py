# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/13 4:41 PM

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # method-1: stack
        n = len(s)
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                # 入栈
                stack.append(i)
            else:
                # 出栈
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
    
        # method-2: greedy, travel twice
        left, right, res = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * right)
            elif left > right:
                left, right = 0, 0 
        return res

        
if __name__ == '__main__':
    s = ")()()(()"
    obj = Solution()
    print(obj.longestValidParentheses(s))