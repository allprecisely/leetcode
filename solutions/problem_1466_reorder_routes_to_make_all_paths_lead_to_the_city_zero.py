# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        ordered_graph = defaultdict(set)
        for (start, end) in connections:
            graph[start].add(end)
            graph[end].add(start)
            ordered_graph[start].add(end)

        self.res = 0
        def dfs(start: int, prev: int) -> None:
            for neigbour in graph[start]:
                if neigbour != prev:
                    dfs(neigbour, start)
                    if start not in ordered_graph[neigbour]:
                        self.res += 1
        
        dfs(0, -1)
        return self.res
