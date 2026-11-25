class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        
        def helper(index):
            if index >= len(cost):
                return 0
            
            if index in cache:
                return cache[index]
            ans = cost[index] + min(helper(index + 1), helper(index + 2))
            cache[index] = ans
            
            return ans
        
        return min(helper(0), helper(1))