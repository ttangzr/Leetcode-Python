# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/12 8:48 AM

from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # method-1: BFS
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        visited = set(beginWord)
        level = 1
        while queue:
            for _ in range(len(queue)):
                word_q = queue.pop(0)
                for word in wordList:
                    if self.isConnected(word_q, word):
                        if word == endWord:
                            return level + 1
                        elif word not in visited:
                            queue.append(word)
                            visited.add(word)
                if word_q in wordList:
                    wordList.remove(word_q)
            level += 1
        return 0

    def isConnected(self, s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(obj.ladderLength(beginWord, endWord, wordList))