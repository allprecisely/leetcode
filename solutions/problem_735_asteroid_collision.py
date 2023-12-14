# https://leetcode.com/problems/asteroid-collision/description/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for asteroid in asteroids[1:]:
            while len(stack) != 0:
                if stack[-1] > 0:
                    if asteroid > 0:
                        stack.append(asteroid)
                    elif stack[-1] < -asteroid:
                        stack.pop()
                        continue
                    elif stack[-1] == -asteroid:
                        stack.pop()
                else:
                    stack.append(asteroid)
                break
            else:
                stack.append(asteroid)
        return stack
