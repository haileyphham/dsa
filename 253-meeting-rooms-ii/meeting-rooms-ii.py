class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) # sort the start times (they get a room first)
        min_heap = [] 
        
        for start, end in intervals: #allows us to get the first and second element in list
            if min_heap and start >= min_heap[0]: #if meeting starts after a meeting ends
                heapq.heappop(min_heap) #the room becomes empty and then we add a new ending time
                
            heapq.heappush(min_heap, end) #if min_heap is empty, or if start < min_heap[0](meeting starts before one ends), we need a new room

        return len(min_heap) #len(heap) is how many rooms we have that overlap
         