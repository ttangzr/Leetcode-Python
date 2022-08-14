# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 5:21 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串
#
class Solution:
    def ReverseSentence(self , str: str) -> str:
        # write code here
        str_list = str.split(' ')
        return ' '.join(str_list[::-1])