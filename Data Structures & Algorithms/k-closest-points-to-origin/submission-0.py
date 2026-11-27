import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = []
        heapq.heapify(euclidean)

        for point in points:
            x1, y1 = point
            dist = math.sqrt((x1)**2 + (y1)**2)
            heapq.heappush(euclidean, (dist, x1, y1))

        resultPoints = []
        for i in range(k):
            dist, x, y = heapq.heappop(euclidean)
            resultPoints.append((x,y))

        return resultPoints