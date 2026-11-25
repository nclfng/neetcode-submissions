class Solution:
    def tribonacci(self, n: int) -> int:
        values = {}
        values[0] = 0
        values[1] = 1
        values[2] = 1
        
        for i in range(3, n+1):
            curr = values[i-1] + values[i-2] + values[i-3]
            values[i] = curr
        
        return values[n]