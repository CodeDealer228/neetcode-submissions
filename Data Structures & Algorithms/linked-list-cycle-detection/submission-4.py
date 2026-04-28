# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vizited = set()
        node = head
        while True:
            if node in vizited:
                return True
            vizited.add(node)

            if node and node.next:
                node = node.next
            else:
                return False
        return False