class Solution:
    def maxProduct(self, n: int) -> int:
        count = 0
        new_int = str(n)

        for i in range(len(new_int)):
            for j in range(i + 1, len(new_int)):
                if int(new_int[i]) * int(new_int[j]) > count:
                    count = int(new_int[i]) * int(new_int[j])

        return count
