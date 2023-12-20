# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1, heap2 = [], []
        if len(costs) > 2 * candidates:
            heap1, heap2 = costs[:candidates], costs[-candidates:]
        else:
            heap1, heap2 = costs, []
        heapq.heapify(heap1)
        heapq.heapify(heap2)

        total_cost = 0
        left, right = candidates, len(costs) - candidates - 1
        while k and left <= right:
            if heap1[0] <= heap2[0]:
                total_cost += heapq.heappop(heap1)
                heapq.heappush(heap1, costs[left])
                left += 1
            else:
                total_cost += heapq.heappop(heap2)
                heapq.heappush(heap2, costs[right])
                right -= 1
            k -= 1
        
        while k:
            if heap1:
                if heap2 and heap2[0] < heap1[0]:
                    total_cost += heapq.heappop(heap2)
                else:
                    total_cost += heapq.heappop(heap1)
            elif heap2:
                total_cost += heapq.heappop(heap2)
            k -= 1
        
        return total_cost
        