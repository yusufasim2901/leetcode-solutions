import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [math.comb(rowIndex , k) for k in range(rowIndex + 1)]
        return a