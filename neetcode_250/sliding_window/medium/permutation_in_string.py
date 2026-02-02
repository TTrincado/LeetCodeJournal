class Solution:
    """
    Iterate through 's2' creating a fresh frequency map for every substring 
    of length len(s1).

    Time Complexity: O(N * M) -> For every step in M (s2), we iterate N (s1).
                     This will TLE (Time Limit Exceeded) on large inputs.
    Space Complexity: O(1) (Map is max 26 chars).
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        count1 = defaultdict(int)

        for s in s1:
            count1[s] += 1  # O(26) max -> O(1) space

        l, r = 0, len(s1)

        while r <= len(s2):  # O(len(s2)) -> O(m)
            count2 = defaultdict(int)  # Refresh the hm

            while l < r:
                # For each letter present in the sliding window (size s1)
                count2[s2[l]] += 1
                # update count2: O(len(s1)) -> O(n)
                l += 1

            if count2 == count1:  # O(1)
                return True
            else:
                r += 1
                l = r - len(s1)

        return False
