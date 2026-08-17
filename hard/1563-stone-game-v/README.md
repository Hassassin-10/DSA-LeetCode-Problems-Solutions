# Stone Game V

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

 
Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.


Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28


Example 3:

Input: stoneValue = [4]
Output: 0


 
Constraints:


	1 <= stoneValue.length <= 500
	1 <= stoneValue[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 2087 ms (beats 58.82%)  
**Memory:** 53.9 MB (beats 35.69%)  
**Submitted:** 2026-08-17T13:11:55.305Z  

```py
from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Alice keeps the left side.
                    #
                    # If left * 2 <= ans, this split cannot
                    # possibly improve the current answer.
                    if left * 2 <= ans:
                        continue

                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # Alice keeps the right side.
                    #
                    # As k increases, right only gets smaller,
                    # so if right * 2 <= ans, all later splits
                    # are useless.
                    if right * 2 <= ans:
                        break

                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)
```

---

[View on LeetCode](https://leetcode.com/problems/stone-game-v/)