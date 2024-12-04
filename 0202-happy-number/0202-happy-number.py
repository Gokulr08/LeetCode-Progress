class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = get_next(n)
        return n == 1