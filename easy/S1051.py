class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        sorted_list = sorted(heights)
        for a, b in zip(heights, sorted_list):
            if a != b:
                count += 1
        return count