from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        First approach
        """
        counter = Counter(nums)  # Counts, lineal O(n) time n' space
        return counter.most_common()[0][0]  # Sorts -> +O(nlog(n))

    def majorityElement2(self, nums: list[int]) -> int:
        """
        Boyer-Moore algorithm. Proves that we can find
        the majority element in O(n) time and O(1) space.

        Reminds me of "Passing the baton".
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
