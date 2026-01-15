class Solution:
    """
    Uses the same logic used in valid palindrome 1, but since we have 
    to check inside an if the time complexity rises to O(n^2).

    Time complexity: O(n^2).
    Space complexity: O(n), for poss.
    """

    def isPalindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True

        for i in range in len(s):
            poss = s[:i] + s[i + 1:]
            if self.isPalindrome(poss):
                return True

        return False


class Solution2:
    """
    Two-Pointer approach: Check for a missmatch and check if forgiving that letter produces a palindrome.

    Time complexity: O(n).
    Space complexity: O(n) for the storage of both skip strings.
    """

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                skip_i = s[i+1: j+1]
                skip_j = s[i: j]

                return (skip_i == skip_i[::-1]) or (skip_j == skip_j[::-1])

            i += 1
            j -= 1

        return True


class Solution3:
    """
    Same two-Pointer approach: Check for a missmatch and check if forgiving that letter produces a palindrome.

    By creating a function that checks if it's a palindrome, we can manage to improve the space complexity to O(1).

    Time complexity: O(n).
    Space complexity: O(1).
    """

    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1))
            l += 1
            r -= 1

        return True
