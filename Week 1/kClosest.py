class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #d = sqrt((x)^2 + (y)^2)
        heap = []
        
        for x, y in points:
            heapq.heappush(heap,((math.sqrt(x**2 + y**2)),[x, y]))
        output = []
        k = 1
        while heap and k <= K:
            h = heapq.heappop(heap)
            output.append(h[1])
            k += 1
        return output
            
        
        
