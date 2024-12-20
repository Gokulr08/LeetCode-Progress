class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels  = ['a', 'A', 'e', 'i', 'o', 'u', 'E', 'I', 'O', 'U']
        n = len(s)
        if n == 1:
            return s
        s_list = list(s)
        left, right = 0, n - 1 

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

            
        return ''.join(s_list)