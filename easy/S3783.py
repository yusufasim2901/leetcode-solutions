import math
class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = str(n)[::-1]
        b = int(a)
        return abs(n - b)
