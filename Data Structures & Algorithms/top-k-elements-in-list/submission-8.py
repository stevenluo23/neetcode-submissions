import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a heap to store the most frequent elements always at the top
        # remove k elements from the heap, logn heap pop each time

        count = {}
        heap = []
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, freq in count.items():
            # max heap, keep freq as first item to compare
            heapq.heappush(heap, (-freq, n))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

