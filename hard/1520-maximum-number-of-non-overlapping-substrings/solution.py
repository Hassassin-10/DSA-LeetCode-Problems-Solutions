class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Track the first and last occurrence of each character
        left = {}
        right = {}
        for i, char in enumerate(s):
            if char not in left:
                left[char] = i
            right[char] = i

        valid_intervals = []

        # Step 2: For each character, try to find a valid self-contained substring interval
        for char in left:
            l = left[char]
            r = right[char]
            is_valid = True
            
            i = l
            while i <= r:
                curr_char = s[i]
                # If a character inside expands left before 'l', then 'l' is invalid
                if left[curr_char] < l:
                    is_valid = False
                    break
                # Expand right boundary to include all occurrences of 'curr_char'
                r = max(r, right[curr_char])
                i += 1
            
            if is_valid:
                valid_intervals.append((l, r))

        # Step 3: Sort candidate intervals by their end index (Greedy choice)
        valid_intervals.sort(key=lambda x: x[1])

        result = []
        last_end = -1

        for l, r in valid_intervals:
            # Pick non-overlapping intervals
            if l > last_end:
                result.append(s[l : r + 1])
                last_end = r

        return result