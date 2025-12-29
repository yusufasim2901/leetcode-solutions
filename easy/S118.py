import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = lambda numRows: [[math.comb(i, j) for j in range(i + 1)] for i in range(numRows)]
        return pascal(numRows)