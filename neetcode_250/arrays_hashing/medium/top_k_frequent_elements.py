class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Uses Counter from collections for the most_common method, which sorts and counts the array.

        Time complexity: O(nlog(k))
        Space complexity: O(n)
        """
        from collections import Counter

        counter = Counter(nums)
        top_k_items = counter.most_common(k)
        return [item[0] for item in top_k_items]


class Solution2:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        We use a counter and a frequency table to store the numbers.
        In this frequency table, the index represents the frequency and the value the numbers that appear that many times.

        The maximum number of times a number can be repeated is equal to the length of the list, so we can set the length of the
        table to the length + 1 (to count for freq=0).

        Time complexity: O(n)
        Space complexity: O(n)
        """
        from collections import defaultdict

        hashmap = defaultdict(int)
        freq_table = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] += 1

        items = list(hashmap.items())

        for i in range(len(items)):
            freq_table[items[i][1]].append(items[i][0])

        res = []
        for i in range(len(freq_table) - 1, 0, -1):
            for n in freq_table[i]:
                res.append(n)

                if len(res) == k:
                    return res
