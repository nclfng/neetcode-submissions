import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # return min number of cpu cycles required to complete all tasks
        heap = []
        heapq.heapify(heap)

        hashMap = {}
        for task in tasks:
            if task in hashMap:
                hashMap[task] += 1
            else:
                hashMap[task] = 1
        
        for value in hashMap.values():
            heapq.heappush(heap, -value)
        
        queue = deque()

        time = 0
        while heap or queue:
            time += 1

            if heap:
                currCount = abs(heapq.heappop(heap))
                currCount -= 1

                if currCount > 0:
                    queue.append((-currCount, time + n))
                
            if queue and queue[0][1] == time:
                count, ready = queue.popleft()
                heapq.heappush(heap, count)
        
        return time