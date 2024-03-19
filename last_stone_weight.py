class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            first = heapq._heappop_max(stones)
            diff = first - stones[0]

            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)

        stones.append(0)
        return stones[0]
