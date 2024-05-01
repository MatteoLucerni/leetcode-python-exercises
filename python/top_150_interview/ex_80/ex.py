class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique = []

        for num in nums:
            if unique.count(num) >= 2:
                continue
            else:
                unique.append(num)

        nums[:] = unique[:]

        return len(nums)


sol = Solution()

# ex1
nums = [1, 1, 1, 2, 2, 3]
print(sol.removeDuplicates(nums))
print(nums)

# ex1
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(sol.removeDuplicates(nums))
print(nums)
