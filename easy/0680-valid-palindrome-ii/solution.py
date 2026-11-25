class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return ispalin(s[i+1:j+1]) or ispalin(s[i:j])
            i += 1
            j -= 1
        return True