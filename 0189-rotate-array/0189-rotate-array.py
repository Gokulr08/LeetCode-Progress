class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # print(nums[-k:])
        l = len(nums)
        for i in range(k):
            # for j in range(len(nums)-k):
            nums.insert(0, nums[-1])
            nums.pop(l)

        return nums