# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/10 09:28 PM

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # method-1: hash table
        ht = defaultdict(list)
        for ss in strs:
            count = [0] * 26
            for ch in ss:
                count[ord(ch) - ord('a')] += 1
            ht[tuple(count)].append(ss)
        return list(ht.values())

        
if __name__ == '__main__':
    obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(obj.groupAnagrams(strs))