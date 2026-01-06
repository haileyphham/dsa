class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
            
        while len(heap)>1:
            y = -heapq.heappop(heap) #this one is bigger
            x = -heapq.heappop(heap)

            if x == y:
                continue
            if x != y:
                 y -= x
                 heapq.heappush(heap, -y)
        return -heapq.heappop(heap) if len(heap) == 1 else 0

            





            
        