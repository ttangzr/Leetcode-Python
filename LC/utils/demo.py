# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/15 20:00
# demo zone

from typing import List
from collections import deque, defaultdict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums

def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        swap(nums, i, min_idx)
    return nums

def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = tmp
    return nums


def quick_sort(nums, l, r):
    if r >= l:
        return
    p = partition(nums, l, r)
    quick_sort(nums, l, p - 1)
    quick_sort(nums, p + 1, r)

def partition(nums, l, r):
    import random
    random_index = random.randint(l, r)
    swap(nums, random_index, l)
    pivot = nums[l]
    lt = l
    # [l, lt] < pivot
    # [lt + 1, i) >= pivot
    for i in range(l + 1, r + 1):
        if nums[i] < pivot:
            lt += 1
            swap(nums, i, lt)
    swap(nums, l, lt)
    return lt

def heap_sort(nums):
    for i in range(len(nums) - 1, -1, -1):
        max_heapify(nums, i, len(nums))
    for i in range(len(nums) - 1, -1, -1):
        swap(nums, i, 0)
        max_heapify(nums, 0, i)

def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 <= heap_len - 1:
        l, r = p * 2 + 1, p * 2 + 2
        if r >= heap_len or heap[r] < heap[l]:
            nex = r
        else:
            nex = l
        if heap[p] < heap[nex]:
            swap(heap, p, nex)
            p = nex
        else:
            break

def merge_sort(nums, l, r):
    if r >= l:
        return
    mid = (l + r) >> 1
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    while i <= mid or j <= r:
        if i > mid or (j <= r and nums[j] < nums[i]):
            tmp.append(nums[j])
            j += 1
        else:
            tmp.append(nums[i])
            i += 1
    nums[l: r + 1] = tmp


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 更新node位置, moveToHead
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 添加node，addToHead
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            # 检查size, removeTail
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 更新node位置，moveToHead
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 抢当前num: dp[i] = dp[i-2] + nums[i]
        # 不抢当前num: dp[i] = dp[i-1]
        # dp[i] = max{dp[i-1], dp[i-2] + nums[i]}
        # dp[0] = nums[0]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # return self.dfs(root, targetSum, [])

        if not root:
            return 0
        return self.countPath(root, targetSum) + \
               self.pathSum(root.left, targetSum) + \
               self.pathSum(root.right, targetSum)

    def dfs(self, root, targetSum, sum_list):
        if not root:
            return 0
        # sum_list: [n1, n1+s1, ..., n1+sn], n1:root.val
        # update sum_list
        sum_list = [root.val + x for x in sum_list]
        # add root.val
        sum_list.append(root.val)
        # traversal
        for num in sum_list:
            if num == targetSum:
                self.count += 1
        return self.count + self.dfs(root.left, targetSum, sum_list) + self.dfs(root.right, targetSum, sum_list)

    def countPath(self, root, targetSum):
        # 以root为起点递归查找targetSUm
        if not root:
            return 0
        count = 0
        if root.val == targetSum:
            count += 1
        left = self.countPath(root.left, targetSum - root.val)
        right = self.countPath(root.right, targetSum - root.val)
        return count + left + right

class Solution:
    def __init__(self):
        self.len = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.len

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.len = max(self.len, left + right + 1)
        return max(left, right) + 1

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # method-1: 双递归
        if not s and not t:
            return True
        if not s or not t:
            return False
        else:
            # s为父二叉树，t为子二叉树，注意用or
            return self.isSameTree(s, t) \
                   or self.isSameTree(s.left, t) \
                   or self.isSameTree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return s.val == t.val \
                   and self.isSameTree(s.left, t.left) \
                   and self.isSameTree(s.right, t.right)

class Solution:
    def quick_sort(self, nums, left, right):
        if right >= left:
            return
        p = self.partition(nums, left, right)
        self.quick_sort(nums, left, p - 1)
        self.quick_sort(nums, p + 1, right)

    def partition(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[left], nums[rand_idx] = nums[rand_idx], nums[left]
        pivot = nums[left]
        lt = left
        # all in [left + 1, lt] < pivot
        # all in [lt, i) >= pivot
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
        nums[lt], nums[left] = nums[left], nums[lt]
        return lt

    def heap_sort(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            self.max_heapify(nums, i, len(nums))
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)


    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 <= heap_len - 1:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) >> 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False

if __name__ == "__main__":
    obj = Solution1()
    matrix = [[-1,3]]
    target = 3
    print(obj.searchMatrix(matrix, target))















