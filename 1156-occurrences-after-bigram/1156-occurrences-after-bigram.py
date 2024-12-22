class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        a = text.split()
        ans = []
        for i in range(len(a)-1):
            if a[i] == first and a[i+1] == second and i+2 < len(a):
                ans.append(a[i+2])
        return ans