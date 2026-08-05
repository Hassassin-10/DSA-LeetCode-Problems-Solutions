# Remove Methods From Project

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

 
Example 1:


Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:



Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.


Example 2:


Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:



Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.


Example 3:


Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:



All methods are suspicious. We can remove them.


 
Constraints:


	1 <= n <= 105
	0 <= k <= n - 1
	0 <= invocations.length <= 2 * 105
	invocations[i] == [ai, bi]
	0 <= ai, bi <= n - 1
	ai != bi
	invocations[i] != invocations[j]

## Solution

**Language:** Python  
**Runtime:** 230 ms (beats 87.88%)  
**Memory:** 99.6 MB (beats 89.39%)  
**Submitted:** 2026-08-05T17:43:24.898Z  

```py
from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # If any non-suspicious method invokes a suspicious one,
        # no methods can be removed.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all remaining (non-suspicious) methods.
        return [i for i in range(n) if not suspicious[i]]
```

---

[View on LeetCode](https://leetcode.com/problems/remove-methods-from-project/)