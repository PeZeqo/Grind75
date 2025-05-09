"""
Runtime 65% O(amount * n)
Memory 56% O(amount)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    minCoins[i] = min(minCoins[i - coin] + 1, minCoins[i])

        return minCoins[amount] if minCoins[amount] != amount + 1 else -1

    # def coinChangeAttempt1(self, coins: List[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0
    #
    #     coins = sorted(coins)
    #     amountToCoins = [math.inf] * (amount + 1)
    #
    #     def dfs(amountLeft: int, coinInd: int, coinSoFar: int):
    #         print(amountLeft, coinInd, coinSoFar)
    #         coinAmount = coins[coinInd]
    #         if coinInd == 0:
    #             if amountLeft % coinAmount == 0:
    #                 amountToCoins[0] = min(coinSoFar + (amountLeft // coinAmount), amountToCoins[0])
    #             return
    #
    #         if amountToCoins[amountLeft] != math.inf:
    #             amountToCoins[0] = min(coinSoFar + amountToCoins[amountLeft], amountToCoins[0])
    #             return
    #
    #         for coinsAdded in range((amountLeft // coinAmount), -1, -1):
    #             newAmountLeft = amountLeft - (coinsAdded * coinAmount)
    #             newCoinsSoFar = coinSoFar + coinsAdded
    #             amountToCoins[amount - newAmountLeft] = min(newCoinsSoFar, amountToCoins[amount - newAmountLeft])
    #             dfs(newAmountLeft, coinInd - 1, newCoinsSoFar)
    #             if amountToCoins[0] != math.inf:
    #                 return
    #
    #     dfs(amount, len(coins) - 1, 0)
    #     return amountToCoins[0] if amountToCoins[0] != math.inf else -1
