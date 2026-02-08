class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        uzaklik1 = abs(z - x)
        uzaklik2 = abs(z - y)
        if uzaklik2 > uzaklik1:
            return 1
        elif uzaklik2 < uzaklik1:
            return 2
        elif uzaklik2 == uzaklik1:
            return 0
        