'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # method-1
        # ans = {('a', 'e' 'r'): ["are", "ear", "era"]}
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

        # method-2 
        # from collections import defaultdict
        # ans = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()


if __name__ == "__main__":
    obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(obj.groupAnagrams(strs))
    print()