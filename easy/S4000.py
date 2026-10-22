class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1

        result = ""

        for i in range(n):
            digit = min(9, s)
            result += str(digit)
            s -= digit

        return int(result)