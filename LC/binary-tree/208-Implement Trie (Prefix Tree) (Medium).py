#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 4:42 下午
# @Author  : T-
# @Site    : 
# @File    : 208-Implement Trie (Prefix Tree) (Medium).py
# @Software: PyCharm

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        self.recursive_insert(word, self.trie)

    def search(self, word: str) -> bool:
        return self.recursive_search(word, self.trie)
    
    def startsWith(self, prefix: str) -> bool:
        return self.recursive_search_prefix(prefix, self.trie)
    
    def recursive_insert(self, word, tree):
        if len(word) == 0:
            tree['#'] = '#'
            return
        if word[0] not in tree:
            tree[word[0]] = {}
        self.recursive_insert(word[1:], tree[word[0]])
        return tree
    
    def recursive_search(self, word, tree):
        if len(word) == 0:
            if '#' in tree:
                return True
            return False
        if word[0] not in tree:
            return False
        return self.recursive_search(word[1:], tree[word[0]])
    
    def recursive_search_prefix(self, word, tree):
        if len(word) == 0:
            return True
        if word[0] not in tree:
            return False
        return self.recursive_search_prefix(word[1:], tree[word[0]])


if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    trie = Trie1()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))