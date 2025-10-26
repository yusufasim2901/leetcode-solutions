class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        kelimeler_listesi = s.split()
        son_kelime = kelimeler_listesi[-1]
        return len(son_kelime) 