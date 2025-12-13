import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        a = math.log(n , 4)
        if a == int(a):
            return True
        else:
            return False