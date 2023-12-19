# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value
        
        visited = set()
        def dfs(divider, dividend):
            result = -1
            visited.add(divider)
            for key, value in graph[divider].items():
                if key == dividend:
                    result = value
                    break
                elif key not in visited:
                    inner_result = dfs(key, dividend)
                    if inner_result != -1:
                        result = value * inner_result
                        break
            visited.remove(divider)
            return result
        
        return [dfs(*query) for query in queries]
