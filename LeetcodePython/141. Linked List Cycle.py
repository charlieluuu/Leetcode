from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # two pointers
        slow, fast = head, head

        # slow runner move 1 step, fast runner move 2 steps per iteration
        # if fast runner meets slow one somewhere, then there is a cycle in linked list

        while fast and fast.next:

            slow, fast = slow.next, fast.next.next

            if slow is fast:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.hasCycle([3,2,0,-4])
    print(result)