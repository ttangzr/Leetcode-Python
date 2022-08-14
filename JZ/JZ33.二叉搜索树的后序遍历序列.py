# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 9:28 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sequence int整型一维数组
# @return bool布尔型
#
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        # method-1: DFS
        if not sequence:
            return False
        len_seq = len(sequence)
        root = sequence[-1]
        # index of right subtrees
        right_index = len_seq - 1
        for i in range(len_seq):
            if sequence[i] > root:
                right_index = i
                break
        # check value of right subtrees
        for i in range(right_index, len_seq - 1):
            if sequence[i] < root:
                return False
        # divide-and-conquer
        left = self.VerifySquenceOfBST(sequence[0:right_index]) \
            if right_index > 0 else True
        right = self.VerifySquenceOfBST(sequence[right_index:-1]) \
            if right_index < len_seq -1 else True
        return left and right

        # method-1: stack
        if not sequence:
            return False
        inorder = sorted(sequence)  # inorder of BST
        # judge pop stack is a valid push stack (inorder)
        return self.isPopOrder(inorder, sequence)

    def isPopOrder(self, pushV, popV):
        n = len(pushV)
        stack = list()
        i, j = 0, 0
        while i < n:
            stack.append(pushV[i])
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
            i += 1
        return j == n
