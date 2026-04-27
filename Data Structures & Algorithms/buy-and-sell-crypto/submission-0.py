class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mins = [None] * n
        maxs = [None] * n

        mins[0] = prices[0]
        maxs[n-1] = prices[n-1]
        for i in range(1,n):
            mins[i] = min(mins[i-1], prices[i])
            maxs[n-1-i] = max(maxs[n-i] ,prices[n-1-i])
                
            
        return max(maxs[i]-mins[i] for i in range(n))

"""
pri [10,1,5,6,7,1]
min [10,1,1,1,1,1]
max [10,7,7,7,7,1]

pri [10,8,7,5,2]
min [10,8,7,5,2]
max [10,8,7,5,2]
"""