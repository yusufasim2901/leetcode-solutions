class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        konum = 1
        yon = 1

        for _ in range(time):
            konum += yon

            if konum == n or konum == 1:
                yon *= -1

        return konum
