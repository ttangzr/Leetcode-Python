# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 20:18


from typing import List


class Solution:
    def getKthElement(self, nums1, nums2, k):
        """
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """
        cur_index1, cur_index2 = 0, 0
        m, n = len(nums1), len(nums2)
        while True:
            # special case
            if cur_index1 == m:
                return nums2[cur_index2 + k - 1]
            if cur_index2 == n:
                return nums1[cur_index1 + k - 1]
            if k == 1:
                return min(nums1[cur_index1], nums2[cur_index2])
            # normal case
            new_index1 = min(cur_index1 + k // 2 - 1, m -1)
            new_index2 = min(cur_index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[new_index1], nums2[new_index2]
            if pivot1 <= pivot2:
                k -= new_index1 - cur_index1 + 1
                cur_index1 = new_index1 + 1
            else:
                k -= new_index2 - cur_index2 + 1
                cur_index2  = new_index2 + 1
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # method-1: binary search
        tot_len = len(nums1) + len(nums2)
        if tot_len % 2 == 1:
            return self.getKthElement(nums1, nums2, (tot_len + 1) // 2)
        else:
            return (self.getKthElement(nums1, nums2, tot_len // 2) + 
                    self.getKthElement(nums1, nums2, tot_len // 2 + 1)) / 2
        
        # method-2: 划分数组
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2 ** 40
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


if __name__ == '__main__':
    nums1 = [1, 3, 4, 9]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    obj = Solution()
    print(obj.findMedianSortedArrays(nums1, nums2))