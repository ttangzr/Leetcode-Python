# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/6 21:26

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # method-1: two stacks
        # left保存往左走，stack保存往右走，准备与后面的碰撞
        left = []
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                # 与stack中的碰撞
                while stack and ast < 0:
                    ast = self.check(ast, stack.pop())
                if ast < 0:
                    left.append(ast)
                elif ast > 0:
                    stack.append(ast)
        return left + stack

        # method-2: one stack
        ans = []    # ast > 0
        for ast in asteroids:
            # collision
            while ans and ast < 0 < ans[-1]:
                if ans[-1] < -ast:
                    ans.pop()
                elif ans[-1] > -ast:
                    break
                else:
                    ans.pop()
                    break
            # ast > 0 or collision free
            else:
                ans.append(ast)
        return ans

    def check(self, l, r):
        if r > -l:
            return r
        elif r < -l:
            return l
        else:
            return 0


if __name__ == '__main__':
    obj = Solution()
    asteroids = [5, 10, -10, -10]
    print(obj.asteroidCollision(asteroids))