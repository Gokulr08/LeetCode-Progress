class Solution:
    def replaceDigits(self, s: str) -> str:
        current_letter=""

        ans=""

        for i in s:
            if i.isalpha():
                current_letter = i
                ans = ans+i
            else:
                a = ord(current_letter)+int(i)
                ans = ans+chr(a)
        return ans