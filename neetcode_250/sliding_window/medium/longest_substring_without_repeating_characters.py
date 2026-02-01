class Solution:
    """
    Creates a dictionary that maps the char with its index and iterates with the window.
    
    Time Complexity: O(N) - One pass only.
    Space Complexity: O(min(N, M)) - HashMap stores unique characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # Char -> Index
        l = 0
        res = 0

        for i, char in enumerate(s):
            if char in seen:
                # Move 'l' to the right of the old instance of this character.
                # use max() to prevent 'l' from jumping backwards to an index 
                # already excluded from the window.
                l = max(seen[char] + 1, l)
            
            # Update the last seen index of the current character
            seen[char] = i
            
            # Update max length
            res = max(res, i - l + 1)
            
        return res