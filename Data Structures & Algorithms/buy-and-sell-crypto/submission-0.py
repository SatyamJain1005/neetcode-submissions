class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    break
                else:
                    pro = prices[j] - prices[i]
                    if max_pro > pro:
                        continue
                    else:
                        max_pro = pro

        return max_pro