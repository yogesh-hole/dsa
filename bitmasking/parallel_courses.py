from collections import defaultdict
from functools import cache
from itertools import combinations
from typing import List


# Grap [[2, 1], [3, 1], [1, 4]]
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        in_deg = [0] * n

        for prev, nxt in relations:
            adj[prev - 1].append(nxt - 1)
            in_deg[nxt - 1] += 1

        # bit_mask:
        # 1 means not taken
        # 0 mean taken
        # initialize to 1<<n -1

        @cache
        def backtrack(bit_mask):
            if not bit_mask:
                return 0

            catalog = [i for i in range(n) if in_deg[i] == 0 and bit_mask & 1 << i]
            ret = float("inf")
            for k_courses in combinations(catalog, min(k, len(catalog))):
                nxt_bit_mask = bit_mask
                for course in k_courses:
                    nxt_bit_mask ^= 1 << course
                    for parent in adj[course]:
                        in_deg[parent] -= 1

                ret = min(ret, 1 + backtrack(nxt_bit_mask))

                for course in k_courses:
                    for parent in adj[course]:
                        in_deg[parent] += 1
            return ret

        return backtrack((1 << n) - 1)


sol = Solution()
print(sol.minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))
