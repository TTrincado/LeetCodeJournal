class Solution:
    """
    Iterative approach
    Time Complexity: O(N) -> Each node is visited once
    Space Complexity: O(1) -> Two Pointers
    """

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            # Before changing curr.next, we must save where we were going or we
            # won't have curr.next after updating it and won't be able to continue
            nxt = curr.next

            # Point current node backwards to 'prev'
            curr.next = prev

            # The current node is now the 'previous' for the next iteration
            prev = curr

            # Move to the saved next node to continue the process
            curr = nxt

        # When curr becomes None, 'prev' is at the new head of the reversed list
        return prev
