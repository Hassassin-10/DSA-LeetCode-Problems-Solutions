class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):

            left.extend(chr(i + ord('a')) for _ in range(freq[i] // 2))

            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left = "".join(left)
        right = left[::-1]

        return left + middle + right
        