class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        len_code = len(code)
        if k == 0:
            return [0] * len_code
        if len_code == 1:
            return code

        l = []

        if k > 0:
            for i in range(len_code):
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % len_code]
                l.append(total)
        else:
            for i in range(len_code):
                total = 0
                for j in range(1, abs(k) + 1):
                    total += code[(i - j + len_code) % len_code]
                l.append(total)

        return l
