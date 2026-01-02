class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        if b > a:
            return -1
        for i in range(a - b + 1):
            pencere = haystack[i : i + b]
            if pencere == needle:
                return i
        return -1