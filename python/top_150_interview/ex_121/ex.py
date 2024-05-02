class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


# Ex1
sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))

# Ex2
sol = Solution()

prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices))

# Ex3
sol = Solution()

prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))
