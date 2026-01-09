class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Pretty straight forward two-pointer approach with an O(n) time complexity and O(1) space complexity.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

class Solution2:
    def reverseString(self, s: str) -> None:
        """
        There is a built-in function in python that reverses the list in O(n) & O(1), probably does
        the two-pointer approach in the back.
        """
        return s.reverse()

class Solution3:
    def reverseString(self, s: str) -> None:
        """
        There is a version that gives as an input a string and not a list.
        Here we can just do s[::-1], which is also O(n) and O(1).
        """
        return s[::-1]
