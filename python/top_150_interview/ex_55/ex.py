class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return False


sol = Solution()

nums1 = [2, 3, 1, 1, 4]
print(sol.canJump(nums1))

nums2 = [3, 2, 1, 0, 4]
print(sol.canJump(nums2))
