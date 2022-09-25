#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # method-1: short to tall
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            space = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    space -= 1
                if space == 0:
                    ans[i] = person
                    break
        return ans

        # method-2: tall to short
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans.insert(person[1], person)
        return ans


if __name__ == '__main__':
    obj = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(obj.reconstructQueue(people))