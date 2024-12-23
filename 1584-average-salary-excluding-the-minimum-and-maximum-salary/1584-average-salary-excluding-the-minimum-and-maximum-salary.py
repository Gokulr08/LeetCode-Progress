class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        
        total = sum(salary)
        
        avg = total / len(salary)
        
        format_avg = "{:.5f}".format(avg)
        
        return float(format_avg)


            