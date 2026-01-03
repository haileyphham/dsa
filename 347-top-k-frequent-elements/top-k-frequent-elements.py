class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' o(n) time complexity, go through the array and add if seen in dict, up the frequency, if not,add it to the set'''

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # if in dict will return value, else: none
        heap = []
        for num, count in freq.items(): #num iterates through the key and count iterates through the value
            heapq.heappush(heap, (count,num)) #pushes elem onto minheap orders by count (if count same then by num) 
            if len(heap)>k:
                heapq.heappop(heap) 
                #at this point, the heap contains the top k elements as a tuple (num,count)
        return [num for count, num in heap]



