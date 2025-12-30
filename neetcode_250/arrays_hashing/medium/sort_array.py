from collections import defaultdict


class Solution:
    """
    Implements QuickSort algorithm.

    Avg. and best case time complexity of O(nlog(n)) but a worst case
    time complexity of O(n^2).

    Space complexity worst case O(n), avg. and best case O(log(n))
    """

    def partition(self, nums: list[int], left: int, right: int) -> int:
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] > nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] > nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] < pivot:
                    break
            while True:
                j -= 1
                if not nums[j] > pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def quickSort(self, nums: list[int], left: int, right: int) -> None:
        if right <= left + 1:
            if right == left + 1 and nums[right] < nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            return

        j = self.partition(nums, left, right)
        self.quickSort(nums, left, j - 1)
        self.quickSort(nums, j + 1, right)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums


class Solution2:
    """
    Implements MergeSort algorithm.

    Time complexity: O(nlog(n)) in all cases.
    Space complexity: O(n).
    """

    def merge_sort(self, arr):
        # Base case
        if len(arr) <= 1:
            return arr

        # Pointer to the mid pivot.
        # Note: // rounds the result down. If len is 5, mid is 2.
        mid = len(arr)//2

        # Recursevly divides until base cases
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        """
        This function takes 2 sorted lists and merges them into
        a single sorted list.
        """
        res = []
        i, j = 0, 0  # Our pointers for the left (i) and right (j) lists

        # ---------------------------------------------------------
        # left = [2, 5]   (i starts here)
        # right = [1, 3]  (j starts here)
        # res = []
        # ---------------------------------------------------------

        # While both lists have elements yet to be compared
        while i < len(left) and j < len(right):
            # Picture 3 pointers. One in the first element of the left list, one in the first
            # of the right, and one in the upper level.

            # --- ITERATION 1 ---
            # left:  [2, 5]      right: [1, 3]
            #         ^ (i=0)            ^ (j=0)
            #
            # Compare: ¿left[0] (2) < right[0] (1)? -> NO.
            # Action: Insert right (1) and advance j.
            # res ahora es: [1]

            # --- ITERATION 2 ---
            # left:  [2, 5]      right: [1, 3]
            #         ^ (i=0)               ^ (j=1)
            #
            # Compare: ¿left[0] (2) < right[1] (3)? -> SÍ.
            # Action: Insert left (2) and advance i.
            # res ahora es: [1, 2]

            # --- ITERATION 3 ---
            # left:  [2, 5]      right: [1, 3]
            #            ^ (i=1)            ^ (j=1)
            #
            # Compare: ¿left[1] (5) < right[1] (3)? -> NO.
            # Action: Insert right (3) and advance j.
            # res ahora es: [1, 2, 3]

            # --- WHILE ENDS ---
            # Now j equals 2. Since len(right) is 2, the while condition ends.

            # Actual code:
            # Compare the current left element with the current right one
            if left[i] < right[j]:
                # If the left one is smaller, we append it to the result
                res.append(left[i])
                i += 1  # Pointer advances
            else:
                # If the right one is bigger or equal, we append it to the result
                res.append(right[j])
                j += 1  # Pointer advances

        # ---------------------------------------------------------
        # LEFT OVER CLEANING: Elements that weren't compared.
        # ---------------------------------------------------------
        # Until now:
        # i = 1 (points to 5)
        # j = 2 (out of index)
        # res = [1, 2, 3]

        # Add left over of 'left' ([5])
        res += left[i:]
        # res: [1, 2, 3, 5]

        # Add left over of right. In this case, nothing.
        res += right[j:]

        return res

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.merge_sort(nums)


class Solution3:
    """
    Implements HeapSort algorithm.

    Time complexity: O(nlog(n)) in all cases.
    Space complexity: O(1) as it sorts in-place.
    """

    def sortArray(self, nums: list[int]) -> list[int]:
        self.heapSort(nums)
        return nums

    def heapify(self, arr, n, i):
        l = (i << 1) + 1
        r = (i << 1) + 2
        largestNode = i

        if l < n and arr[l] > arr[largestNode]:
            largestNode = l

        if r < n and arr[r] > arr[largestNode]:
            largestNode = r

        if largestNode != i:
            arr[i], arr[largestNode] = arr[largestNode], arr[i]
            self.heapify(arr, n, largestNode)

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)


class Solution4:
    """
    Implements CountingSort algorithm.
    """

    def sortArray(self, nums: list[int]) -> list[int]:
        def counting_sort():
            count = defaultdict(int)
            minVal, maxVal = min(nums), max(nums)
            for val in nums:
                count[val] += 1

            index = 0
            for val in range(minVal, maxVal + 1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1

        counting_sort()
        return nums
