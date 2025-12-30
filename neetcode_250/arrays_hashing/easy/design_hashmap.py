class MyHashMap:
    """
    Strategy: Take advantage of the direct access of an array if an index is given
    by creating a large array where the index will be the key and its value, the value.

    Time complexity: O(1) for each operation.
    Space complexity: O(m), with m the size of the array.
    """

    def __init__(self):
        self.map = [-1] * 10000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1
