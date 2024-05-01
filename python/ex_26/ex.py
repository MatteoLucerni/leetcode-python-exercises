class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique = []

        for num in nums:
            if num in unique:
                continue
            else:
                unique.append(num)

        nums[:] = unique[:]

        return len(nums)


sol = Solution()

# ex 1
nums = [1, 1, 2]

print(sol.removeDuplicates(nums))
print(nums)

# ex 2
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(sol.removeDuplicates(nums))
print(nums)
