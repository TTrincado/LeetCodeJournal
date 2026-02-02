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


class Solution2:
    """
    1. Use a HashMap ('count') to track frequencies of all chars in the current window.
    2. Track 'max_f', representing the frequency of the most dominant character 
       in the current window.
    3. Determine validity dynamically:
       - If (Window Length - max_f) > k, we have too many replacements to make.
       - Shrink window from left.

    Optimization Logic:
    We do not need to decrement 'max_f' when shrinking. 
    We only care about finding a window larger than the current 'res'. 
    To beat 'res', we need a larger 'max_f'. A smaller 'max_f' (caused by shrinking) 
    won't produce a new record, so keeping the 'stale' high value is safe for this specific metric.

    Time Complexity: O(N).
    Space Complexity: O(M) - Map stores at most 26 keys -> O(1).
    """

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_f = 0

        for r in range(len(s)):
            # Add current char to map
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update the count of the dominant character in the window
            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1  # Remove left char from map
                l += 1
                # NOTE: We don't update max_f here. It's an optimization.
                # Even if max_f is technically lower now, we only care if we
                # find a new max_f that allows a bigger window later.

            res = max(res, r - l + 1)

        return res
