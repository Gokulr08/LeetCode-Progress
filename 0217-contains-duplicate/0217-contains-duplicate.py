class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for idx, val in enumerate(nums):
            if val not in numsDict:
                numsDict[val] = 1
            else:
                numsDict[val] +=1

        for contain in numsDict.values():
            if contain > 1:
                return True
            
        return False
