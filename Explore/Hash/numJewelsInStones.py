'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.

'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # # method-1
        # hashMap = {}
        # res = 0
        # for idx, stone in enumerate(S):
        #     if hashMap.get(stone) is not None and stone in J:
        #         hashMap[stone] += 1
        #         res += 1
        #     elif hashMap.get(stone) is None and stone in J:
        #         hashMap[stone] = 1
        #         res += 1
        # return res

        # method-2
        return len([i for i in S if i in J])

        # # method-3
        # return sum([S.count(x) for x in J])
            
        

if __name__ == "__main__":
    obj = Solution()
    print(obj.numJewelsInStones("z", "Z"))