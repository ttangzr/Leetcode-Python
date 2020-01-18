'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method-1
        # length = len(nums)
        # nums.sort()
        # if length == 1:
        #     return nums[0]
        # if nums[0] != nums[1]:
        #     return nums[0]
        # elif nums[length - 2] != nums[length - 1]:
        #     return nums[length - 1]

        # for i in range(1, length - 2):
        #     if  nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
        #         return nums[i]

        # method-2
        # hashMap = {}
        # for i in nums:
        #     try:
        #         hashMap.pop(i)
        #     except:
        #         hashMap[i] = 1
        # # return and delete the last key-value
        # return hashMap.popitem()[0]

        # method-3
        # XOR:a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        a = 0
        for i in nums:
            a ^= i
        return a


if __name__ == "__main__":
    obj = Solution()
    List = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
    res = obj.singleNumber(List)
    print(res)