class Solution(object):
    def averageValue(self, nums):
        toplam = 0
        count = 0
        for i in nums:
            if i % 6 == 0:
                toplam = toplam + i
                count = count + 1
        if count == 0:
            return 0
        return toplam / count