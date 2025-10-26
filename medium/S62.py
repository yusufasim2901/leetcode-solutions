import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m + n - 2
        sonuc = math.factorial(a) / (math.factorial(m - 1) * math.factorial(n - 1))
        return int(sonuc)