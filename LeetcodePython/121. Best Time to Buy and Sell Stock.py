class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0
        # iterate to find the lowest price compare to the first index and keep findng is there any lowest price
        for price in prices[1:]:
            if buy_price > price:
                buy_price = price
            # always compare to every single profit
            profit = max(profit, price - buy_price)

        return profit


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(result)