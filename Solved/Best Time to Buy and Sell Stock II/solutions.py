class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if min_price < price:
                max_profit += price - min_price

            min_price = price

        return max_profit
    