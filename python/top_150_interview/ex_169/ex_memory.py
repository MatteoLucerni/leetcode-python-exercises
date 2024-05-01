class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        best = None

        for num in nums:
            if count == 0:
                best = num
            count += 1 if num == best else -1

        return best


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
