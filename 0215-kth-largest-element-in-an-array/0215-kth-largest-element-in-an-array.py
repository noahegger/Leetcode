import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            # add each num to the heap, smallest will be at the beginning
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                # if we exceed k elements, remove the first
                heapq.heappop(min_heap)
        # after going through entire list, heap will be size k
        # and first element will be the kth largest
        return min_heap[0]