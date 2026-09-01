from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Give every litter cell a bit in the mask.
        litter_id = {}
        start = -1
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = r * n + c
                elif classroom[r][c] == 'L':
                    litter_id[r * n + c] = litter_count
                    litter_count += 1

        # No litter to collect.
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1
        mask_count = 1 << litter_count

        # State encoding:
        # ((position * mask_count + mask) * (energy + 1) + remaining_energy)
        #
        # At most:
        # 400 * 1024 * 51 ~= 20.5 million states.
        # bytearray uses only 1 byte per state.
        total_states = m * n * mask_count * (energy + 1)
        visited = bytearray(total_states)

        def encode(pos, mask, en):
            return (pos * mask_count + mask) * (energy + 1) + en

        # Queue stores:
        # (position, collected_mask, remaining_energy, distance)
        #
        # Encode the first three values into one integer to reduce
        # the memory overhead of tuples.
        q = deque()

        initial_state = encode(start, 0, energy)
        visited[initial_state] = 1

        # Store distance separately by BFS layers.
        q.append((start, 0, energy))
        moves = 0

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            for _ in range(len(q)):
                pos, mask, en = q.popleft()

                if mask == full_mask:
                    return moves

                r, c = divmod(pos, n)

                # Cannot make another move without energy.
                # (If we're on R, entering it would already have reset it.)
                if en == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    npos = nr * n + nc
                    nen = en - 1
                    nmask = mask

                    # Collect litter when entering its cell.
                    if npos in litter_id:
                        nmask |= 1 << litter_id[npos]

                    # Reset energy immediately upon entering R.
                    if classroom[nr][nc] == 'R':
                        nen = energy

                    state = encode(npos, nmask, nen)

                    if not visited[state]:
                        visited[state] = 1
                        q.append((npos, nmask, nen))

            moves += 1

        return -1
