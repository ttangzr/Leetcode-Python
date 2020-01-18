''''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        sum_nums = sum(nums)
        sumLeft = 0
        sumRight = 0
        length = len(nums)
        for i in range(length):
            if sumLeft * 2 == sum_nums - nums[i]:
                return i
            sumLeft += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    List = [-1,-1,0,1,1,1]
    res = s.pivotIndex(List)
    print(res)
    