# https://leetcode.com/problems/number-of-provinces/description/

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        all_cities = set(range(len(isConnected)))
        while all_cities:
            provinces += 1
            to_visit = set([all_cities.pop()])
            while to_visit:
                for city, con in enumerate(isConnected[to_visit.pop()]):
                    if con and city in all_cities:
                        all_cities.remove(city)
                        to_visit.add(city)
        return provinces
                        
    def findCircleNumRecursive(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(city: int) -> None:
            for con, is_con in enumerate(isConnected[city]):
                if is_con and con not in visited:
                    visited.add(con)
                    dfs(con)
        
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1
        
        return provinces

                        