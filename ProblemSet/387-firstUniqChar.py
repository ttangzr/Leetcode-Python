'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method-1
        hashMap = {}
        for idx, lett in enumerate(s):
            if hashMap.get(lett) is None:
                hashMap[lett] = 1
            else:
                hashMap[lett] += 1
        
        for idx, lett in enumerate(s):
            if hashMap.get(lett) == 1:
                return idx
        return -1

        # method-2
        # for idx, lett in enumerate(s):
        #     if lett not in s[:idx] and lett not in s[idx + 1:]:
        #         return idx 
        # return -1

if __name__ == "__main__":
    obj = Solution()
    s = "leetcode"
    print(obj.firstUniqChar(s))