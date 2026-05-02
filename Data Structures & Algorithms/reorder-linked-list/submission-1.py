# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        id_map = {} # int -> ListNode
        id = 0
        current_node = head
        while current_node is not None:
            id_map[id] = current_node
            id+=1
            current_node = current_node.next
        
        sorted_nodes = list(id_map.items())
        sorted_nodes.sort(key = lambda x: x[1].val)
        
        for i in range(len(sorted_nodes)):    
            j = (i+1)//2 
            if i%2==1: j=-j
            id,node = sorted_nodes[j]
                
            if i>0:
                last_node.next = node
            last_node = node
            
        node.next = None



"""
val [8, 4, 6, 2] ->
id   0  1  2  3 

sorted_value [2 4 6 8]
sorted_id     3 1 2 0
res_index = [3, 0, 1, 2]
             2  8  4  6
sorted_value.index(elem)

sort(key = )
[2, 8, 4, 6]
"""

