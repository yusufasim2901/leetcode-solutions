class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = sum(int(r) for r in str(n))
        squareSum = sum(int(r) ** 2 for r in str(n))
        if squareSum - digitSum >= 50:
            return True
        else:
            return False