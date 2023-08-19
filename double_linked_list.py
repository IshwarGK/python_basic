class Node:
    def __init__(self, data) -> None:
        new_node = data
        new_node.next = None
        new_node.prev = None
        
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.head.next = None
        self.head.prev = None 
    
    
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node