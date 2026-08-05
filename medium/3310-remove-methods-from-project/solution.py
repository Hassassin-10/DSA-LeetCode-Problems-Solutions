        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

            graph[u].append(v)
        for u, v in invocations:

        graph = [[] for _ in range(n)]
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
class Solution:

from typing import List
from collections import deque
