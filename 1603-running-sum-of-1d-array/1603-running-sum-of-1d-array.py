class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        sum = 0

        for idx, val in enumerate(nums):
            sum = sum + val
            ans[idx] = sum

        return ans

        