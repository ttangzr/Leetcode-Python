'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method-1
        # might exceed time
        # hashSet = []
        # for i in range(len(nums)):
        #     if nums[i] in hashSet:
        #         return True       
        #     hashSet.append(nums[i])        
        # return False

        # method-2
        nums.sort()
        length = len(nums)
        if length == 1:
            return False
        for i in range(length):
            if nums[i] == nums[i-1]:
                return True
        return False


if __name__ == "__main__":
    obj = Solution()
    List = [3,3]
    res = obj.containsDuplicate(List)
    print(res)