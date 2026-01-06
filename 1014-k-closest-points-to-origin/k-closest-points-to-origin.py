class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #points[i] is a tuple

        #find the distance of the point from 0
        #add the point into a heap ordered by heapq.heappush(heap, (distance[points[i]], points[i]))

        heap = []
        for x, y in points:
            dist = (((x-0)**2) + ((y-0)**2))**0.5
            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
 

        return [point for (_, point) in heap]


        


        
        