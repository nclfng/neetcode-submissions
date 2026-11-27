import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = []
        heapq.heapify(newStones)

        for stone in stones:
            heapq.heappush(newStones, -stone)

        while len(newStones) > 1:
            y = abs(heapq.heappop(newStones))
            x = abs(heapq.heappop(newStones))

            if x < y:
                heapq.heappush(newStones, -(y-x))
        
        if len(newStones) == 1:
            return -newStones[0]
        else:
            return 0