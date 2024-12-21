class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for ind, val in enumerate(s):
            if val in d:
                d[val] += 1
            else:
                d[val] = 1


        c = []
        for i in d.values():
            c.append(i)
        

        for j in range(0, len(c) - 1):
            a = c[j]
            if a != i:
                return False
       
        return True
