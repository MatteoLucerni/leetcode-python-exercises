class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """

        for n in range(k):
            nums.insert(0, nums[len(nums) - 1])
            nums.pop()


def testResult(array, function):
    print("=" * 50)

    print(f"Return: {function}")
    print(f"Array: {array}")


sol = Solution()

# ex1
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
testResult(nums, sol.rotate(nums, k))

# ex1
nums = [-1, -100, 3, 99]
k = 2
testResult(nums, sol.rotate(nums, k))
