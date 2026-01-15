class Solution2:
    """
    Strategy: Sort the words and create a hash map -> { sorted_word: [word1, word2, ...]}

    Time complexity: O(n * klog(k))
    Space complexity: O(n)
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        hashmap = defaultdict(list)
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)

        for value in hashmap.values():
            res.append(value)

        return res


class Solution2:
    """
    Counts the frequency of letters and stores it in a hashmap.

    Time complexity: O(k * n)
    Space complexity: O(k * n)
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
