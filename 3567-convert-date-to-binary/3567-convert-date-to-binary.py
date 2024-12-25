class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = map(int, date.split('-'))
        
        year_binary = bin(year)[2:]
        month_binary = bin(month)[2:]
        day_binary = bin(day)[2:]
        
        return f"{year_binary}-{month_binary}-{day_binary}"
