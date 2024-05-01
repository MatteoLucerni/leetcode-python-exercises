class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new = []

        for n in nums:
            if n != val:
                new.append(n)

        nums[:] = new[:]

        return len(nums)


sol = Solution()

# Example 1
nums = [3, 2, 2, 3]
val = 3

print(sol.removeElement(nums, val), nums)

# Example 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

print(sol.removeElement(nums, val), nums)
