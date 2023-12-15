# https://leetcode.com/problems/number-of-recent-calls/description/

from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        if self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
