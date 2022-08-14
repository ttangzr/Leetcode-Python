# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/6 11:55 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return bool布尔型
#
class Solution:
    def isNumeric(self , str: str):
        # write code here
        # method-1: 正则表达式
        import re
        match = re.match(
            '^\s*[+-]{0,1}((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))([eE][+-]{0,1}[\d]+){0,1}\s*$', str)
        if match:
            return True
        else:
            return False

        # method-2:
        # delete blank space
        front = 0
        while front < len(str) and str[front] == ' ':
            front += 1
        if front < len(str) and (str[front] == '+' or str[front] == '-'):
            front += 1
        last = len(str) - 1
        while last >= front and str[last] == ' ':
            last -= 1
        str = str[front:last + 1]
        return self.isInteger(str) or self.isDecimal(str) or self.isScientific(str)

    def isInteger(self, str: str) -> bool:
        if not str:
            return False
        for i in range(len(str)):
            if not '0' <= str[i] <= '9':
                return False
        return True

    def isDecimal(self, str: str) -> bool:
        if not str:
            return False
        for i in range(len(str)):
            if str[i] == '.':
                left = self.isInteger(str[:i])
                right = self.isInteger(str[i + 1:])
                return (i == 0 and right) or (i == len(str) - 1 and left) or (left and right)
        return False

    def isScientific(self, str: str) -> bool:
        if not str:
            return False
        for i in range(len(str)):
            if str[i] == 'e' or str[i] == 'E':
                left = self.isInteger(str[:i]) or self.isDecimal(str[:i])
                bias = 1 if i < len(str) - 2 and (str[i + 1] == '+' or str[i + 1] == '-') else 0
                right = self.isInteger(str[i + 1 + bias:])
                return left and right
        return False


if __name__ == "__main__":
    obj = Solution()
    # ["+100","5e2","-123","3.1416","-1E-16"]
    # ["12e","1a3.14","1.2.3","+-5","12e+4.3"]
    str = "123.45e+6"
    print(obj.isNumeric(str))


