import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_of_odd = n * n
        sum_of_even = n * (n + 1)
        return math.gcd(sum_of_odd , sum_of_even)