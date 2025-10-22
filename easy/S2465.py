class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        a = sorted(nums)
        distinct_averages = set()
        while a:
            smallest = a.pop(0)  
            largest = a.pop(-1) 
            average = (smallest + largest) / 2
            distinct_averages.add(average)
        return len(distinct_averages)