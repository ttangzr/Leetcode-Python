'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # mothod-1
        # return self.isHappy(sum(int(i) ** 2 for i in str(n))) if n > 4 else n == 1

        # method-2
        # implement slow point and fast point
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"


if __name__ == "__main__":
    obj = Solution()
    print(obj.isHappy(19))