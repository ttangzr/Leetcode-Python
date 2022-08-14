# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 16:23

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str):
        # 单调栈
        stack = []
        visited = set()
        remain_cnt = Counter(s)
        for ch in s:
            if ch not in visited:
                # 保证单调，如果-1元素后续还有，待后续再append
                # 若后续无该元素，则必须append
                while stack and ch < stack[-1] and remain_cnt[stack[-1]] > 0:
                    visited.remove(stack.pop())
                visited.add(ch)
                stack.append(ch)
            remain_cnt[ch] -= 1
        return ''.join(stack)


if __name__ == "__main__":
    obj = Solution()
    s = "cbacdcbc"
    print(obj.removeDuplicateLetters(s))