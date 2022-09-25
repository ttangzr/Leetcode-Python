#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class MapSum:
    def __init__(self):
        self.lookup = {}

    def insert(self, key: str, val: int) -> None:
        self.lookup[key] = val

    def sum(self, prefix: str) -> int:
        val = 0
        for key in self.lookup.keys():
            if key.startswith(prefix):
                val += self.lookup[key]
        return val


if __name__ == "__main__":
    # Your MapSum object will be instantiated and called as such:
    # obj = MapSum()
    # obj.insert(key,val)
    # param_2 = obj.sum(prefix)
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print(mapSum.sum("ap"))     # return 3
    mapSum.insert("app", 2)
    print(mapSum.sum("ap"))  # return 5
    mapSum.insert("apple", 2)
    print(mapSum.sum("ap"))     # return 4