# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/22 8:46 AM


from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.SEG_COUNT = 4
        self.segments = [0] * self.SEG_COUNT
        self.ans = list()
        self.s = None

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.n = len(s)
        if self.n < 4 or self.n > 16:
            return []
        self.s = s
        self.becktracking(0, 0)
        return self.ans

    def becktracking(self, seg_id, seg_start):
        # found 4 segments， backtrack
        if seg_id == self.SEG_COUNT:
            if seg_start == self.n:
                ip = '.'.join(str(seg) for seg in self.segments)
                self.ans.append(ip)
            return
        # traverse all strings, no found 4 segments yet, backtrack
        if seg_start == self.n:
            return
        # if start with 0, this segment must be 0
        if self.s[seg_start] == "0":
            self.segments[seg_id] = 0
            self.becktracking(seg_id + 1, seg_start + 1)
        # general case
        addr = 0
        for seg_end in range(seg_start, self.n):
            addr = addr * 10 + (ord(self.s[seg_end]) - ord("0"))
            if 0 < addr <= 255:
                self.segments[seg_id] = addr
                self.becktracking(seg_id + 1, seg_end + 1)
            else:
                break


if __name__ == '__main__':
    obj = Solution()
    s = "101023"
    print(obj.restoreIpAddresses(s))
