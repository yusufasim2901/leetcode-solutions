class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frekanslar = {}
    
        for num in nums:
            if num in frekanslar:
                frekanslar[num] = frekanslar[num] + 1
            else:
                frekanslar[num] = 1
            
    
        for num, sayi in frekanslar.items():
            if sayi == 1:
                return num