class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data=data)
        
        if not self.head:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node
        
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        
        print(None)
        #print(current_node.data)
        
    def delete(self, position):
        current_node = self.head
        if position == 1:
            delete_node = self.head
            self.head = delete_node.next
            delete_node = None
            
            return True
        count1 = 2
        while current_node:
            if count1 == position:
                delete_node = current_node.next
                current_node.next = delete_node.next
                delete_node = None
                
                return True
            count1 += 1
            current_node = current_node.next
        
        return False
        
if __name__ == "__main__":
    L1 = LinkedList()
    L1.append(10)
    L1.append(20)
    L1.append(30)
    L1.display()
    L1.delete(2)
    L1.display()
    L1.delete(1)
    L1.display()
    
    
        