class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a = high - low
        if low % 2 == 0 and high % 2 == 0:
            return a // 2
        elif low % 2 == 1 and high % 2 == 0:
            return (a // 2) + 1
        elif low % 2 == 0 and high % 2 == 1:
            return (a // 2) + 1
        elif low % 2 == 1 and high % 2 == 1:
            return (a // 2) + 1
        