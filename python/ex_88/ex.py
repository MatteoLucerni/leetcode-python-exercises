class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]

        nums1[:] = nums1 + nums2
        nums1.sort()


sol = Solution()

# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol.merge(nums1, m, nums2, n)

print(nums1)

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0

sol.merge(nums1, m, nums2, n)

print(nums1)

# Example 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1

sol.merge(nums1, m, nums2, n)

print(nums1)
