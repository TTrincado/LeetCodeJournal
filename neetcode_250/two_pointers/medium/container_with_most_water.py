class Solution:
    """
    Two-Pointer approach. The logic here is that the water between each index can be calculated
    as the lower-heighted pillar times the distance between both pillars. For the pointers, we
    start at both ends and move the one that points to the current lower-heighted pillar, so we 
    can test always with the maximum water posibly contained. 

    Time Complexity: O(N) - Single pass through the array.
    Space Complexity: O(1) - Constant extra space.
    """
    def maxArea(self, heights: list[int]) -> int:
        i,j = 0, len(heights) - 1
        res = 0
        current = 0

        while i < j:
            left = heights[i]
            right = heights[j]
            dist = j - i

            current = min(left, right) * dist

            if current > res:
                res = current

            if left > right:
                j -= 1
            else:
                i += 1
        return res