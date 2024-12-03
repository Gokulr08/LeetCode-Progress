from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        
        for letter, count in r_counter.items():
            if m_counter[letter] < count:
                return False
        
        return True