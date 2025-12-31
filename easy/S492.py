import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = math.isqrt(area)
        for i in range(res , 0 , -1):
            if area % i == 0:
                a = i
                b = area // i
                return [b , a]