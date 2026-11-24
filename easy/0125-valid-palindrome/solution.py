
class Solution:
    def filter(self, s):
        st = ""
        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                st += chr(ord(s[i]) + 32)
            elif "a" <= s[i] <= "z" or "0" <= s[i] <= "9":
                st += s[i]
        return st

    def isPalindrome(self, s: str) -> bool:
        f = self.filter(s)
        i, j = 0, len(f) - 1

        while i < j:
            if f[i] != f[j]:
                return False
            i += 1
            j -= 1

        return True
