class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for num in nums:
            if nums.count(num) > len(nums) / 2:
                return num


def testResult(array, function):
    print("=" * 50)

    print(f"Return: {function}")
    print(f"Array: {array}")


sol = Solution()

# ex1
nums = [3, 2, 3]
testResult(nums, sol.majorityElement(nums))

# ex1
nums = [2, 2, 1, 1, 1, 2, 2]
testResult(nums, sol.majorityElement(nums))
