# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = d = 0
        r_present = d_present = True
        while r_present and d_present:
            r_present = d_present = False
            new_round_senate = []
            for c in senate:
                if c == 'R':
                    if d == 0:
                        r_present = True
                        new_round_senate.append(c)
                        r += 1
                    else:
                        d -= 1
                elif r == 0:
                    d_present = True
                    new_round_senate.append(c)
                    d += 1
                else:
                    r -= 1
            print(new_round_senate, r,d)
            senate = new_round_senate
        return "Radiant" if r_present else "Dire"
