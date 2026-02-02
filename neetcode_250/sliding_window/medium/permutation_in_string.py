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


class Solution2:
    """
    More efficient approach, instead of resetting the count2 frequency map, we
    add what is coming in and substract what is coming out of the window, taking O(1) in 
    this step.

    Time Complexity: O(N * 26) -> O(N) (Dictionary comparison takes at most O(26)).
    Space Complexity: O(1) (Max 26 keys).
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        if len(s1) > len(s2):
            return False  # Common pitfall, there can't
        # be substrings in s1 if s1 is bigger, not necessary tho

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for s in s1:
            count1[s] += 1

        l = 0
        for r in range(len(s2)):
            count2[s2[r]] += 1

            # If window is larger than s1, remove outgoing char (Left)
            # We use an 'if' because the window grows 1 by 1, so it exceeds only by 1.
            if (r - l + 1) > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    # Clean up zero-counts for valid comparison, if we skipped
                    # this step they wouldnt be the same because a dict. that contains
                    # a key with value 0 != that doesn't have the value
                    del count2[s2[l]]
                l += 1

            if count1 == count2:
                return True

        return False
