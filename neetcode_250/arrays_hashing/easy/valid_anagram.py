from collections import defaultdict


class Solution:
    """
    Uses a shared hashmap that counts the frequency of the letters in the word.

    Time complexity: O(n) - We iterate through both strings once.
    Space complexity:: O(1) - The map size stays within 26 characters (a-z).
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Strategy: Create a hash map that tracks frequency.
        charmap = defaultdict(int)

        for letter in s:
            charmap[letter] += 1

        for letter in t:
            charmap[letter] -= 1
            # Early exit: If count drops below zero, 't' has extra chars.
            if charmap[letter] < 0:
                return False
        return True


class Solution:
    """
    We can also sort them and compare for an O(nlogn+mlogm) time complexity, and the space complexity depends on the sorting
    algorithm used. sorted() uses an hybrid derived from merge sort and insertion sort, which has a time complexity of O(nlogn)
    in average and worst case, a O(n) best case and a worst case space complexity of O(n).
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
