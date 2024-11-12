import sys
sys.set_int_max_str_digits(10**6)


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = "".join(map(str, num))
        ad = int(res) + k
        s = str(ad)

        s_list = list(map(int, s))
        return s_list

