class Solution:
    """
    1. Identify all unique characters in 's' (max 26).
    2. For each character 'c':
        - Create a sliding window that considerates any other chars as replacements.
        - If Window Length - Count of 'c' > k, the window is invalid:
            - We advance our left pointer until the window is valid again.
            - NOTE: We dont regress our right pointer ever.

    Time Complexity: O(M * N) where M is unique chars (max 26), which is effectively O(N).
    Space Complexity: O(M) to store the set.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)  # Get unique characters

        for c in charSet:
            count = l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                # NOTE on Window Length Calculation (r - l + 1):
                # Since indices 'l' and 'r' are inclusive, we must add 1.
                # Example: A window from index 2 to 4 is [2, 3, 4].
                # Wrong approach -> (r - l): 4 - 2 = 2.
                # Correct approach -> (r - l + 1): 4 - 2 + 1 = 3.
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
