class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = zip(heights , names)
        sorted_combined = sorted(combined , reverse=True)
        result = [name for height  , name in sorted_combined]
        return result