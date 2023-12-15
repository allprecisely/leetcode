# https://leetcode.com/problems/dota2-senate/

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        senate_len = len(senate)
        for i, c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            senate_len += 1
            if r[0] < d[0]:
                r.append(senate_len)
            else:
                d.append(senate_len)
            r.popleft()
            d.popleft()

        return "Radiant" if r else "Dire"
