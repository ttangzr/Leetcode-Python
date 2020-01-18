'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# slide window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        ans = 0
        map = {}
        start = 0
        for end in range(n):
            alpha = s[end]
            if map.get(alpha) is not None: # duplicate
                start = max(map.get(alpha), start)
            ans = max(ans, end - start + 1)
            map[s[end]] = end + 1 # put val
            end += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    string = 'pwwkew'
    ans = s.lengthOfLongestSubstring(string)
    print(ans)
    pass