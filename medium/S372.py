class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337
        res = 1
        
        for num in b:
            res = pow(res, 10, 1337) * pow(a, num, 1337) % 1337
            
        return res