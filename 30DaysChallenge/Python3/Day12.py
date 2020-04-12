class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            if y!=x:
                heapq.heappush(heap, -(y - x))
                
        if len(heap) > 0:
            return -heap[0]
        return 0