class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            j = i*i
            l.append(j)
        return sorted(l)
