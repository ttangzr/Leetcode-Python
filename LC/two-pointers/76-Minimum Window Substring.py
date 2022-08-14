# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/15 22:47
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # method-1: sliding window
        import collections
        # 用defaultdict避免invalid key报错
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_cnt = len(t)
        l = 0
        res = (0, float('inf'))
        for r, ch in enumerate(s):
            if need[ch] > 0:
                need_cnt -= 1
            need[ch] -= 1
            if need_cnt == 0:
                # step1: sliding window包含所有need
                # need={A:0,B:0,C:0,D:-1,O:-1,E:-1}
                while True:
                    # step2: 增加i，缩小窗口排除前面多余元素D,O,E
                    prev_c = s[l]
                    if need[prev_c] == 0:
                        break
                    need[prev_c] += 1
                    l += 1
                # 更新sliding window长度
                if r - l < res[1] - res[0]:
                    res = (l, r)
                # step3: i+1，寻找新的window
                need[s[l]] += 1
                need_cnt += 1
                l += 1
        return "" if res[1] > len(s) else s[res[0]: res[1] + 1]


if __name__ == "__main__":
    obj = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(obj.minWindow(s, t))