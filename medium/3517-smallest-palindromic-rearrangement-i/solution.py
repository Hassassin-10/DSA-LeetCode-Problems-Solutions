
            left.extend(chr(i + ord('a')) for _ in range(freq[i] // 2))

            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left = "".join(left)
        right = left[::-1]

        return left + middle + right
        
