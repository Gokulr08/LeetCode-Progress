class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(32):
            ans = pow(4, i)
            
            if ans == n:
                return True
        return False
