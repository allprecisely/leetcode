# https://leetcode.com/problems/destination-city/description/

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_cities = set()
        incoming_cities = set()
        for path in paths:
            outgoing_cities.add(path[0])
            incoming_cities.add(path[1])
        return (incoming_cities - outgoing_cities).pop()