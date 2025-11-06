import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target % math.gcd(x , y) == 0 and target <= x + y:
            return True
        else:
            return False