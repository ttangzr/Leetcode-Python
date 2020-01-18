'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # method-1
        hashMap = {}
        heap_max = []
        ans = []
        # setup mappings: character of the num it appears
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        # push key-value into heapq
        for num in hashMap:
            import heapq
            heapq.heappush(heap_max, (-hashMap[num], num))
        # pop top K key-value
        for i in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans


        # method-2
        # count = collections.Counter(nums)   
        # return heapq.nlargest(k, count.keys(), key=count.get) 

        # method-3
        # return [i[0] for i in Counter(nums).most_common(k)]

        
        


if __name__ == "__main__":
    obj = Solution()
    print(obj.topKFrequent([1,1,1,2,2,3,3,3,3,3], 2))
            