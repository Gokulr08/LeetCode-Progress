
class Solution:
    from collections import Counter
    def sumOfUnique(self, nums: List[int]) -> int:

        freq = Counter(nums)
        
        unique_sum = sum(num for num, count in freq.items() if count == 1)
        
        return unique_sum