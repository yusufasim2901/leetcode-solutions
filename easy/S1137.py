class Solution:
    def tribonacci(self, n: int) -> int:
            a, b, c = 0, 1, 1
            if n == 0: return 0
            if n < 3: return 1
            for i in range(3, n + 1):
                toplam = a + b + c
                a = b
                b = c
                c = toplam
            return c