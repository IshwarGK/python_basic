class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, data):
        current_node = Node(data=data)
        
        if not self.head:
            self.head = current_node
            return
        
        while self.head.next:
            self.head = self.head.next
            
        self.head.next = current_node
    
    def read_list(self):
        if not self.head:
            print("")
            return
        
        while self.head:
            print(self.head.data)
            self.head = self.head.next 
            
            
if __name__ == "__main__":
    l1 = Linkedlist()
    l1.add(10)
    l1.add(20)
    l1.add(30)

    l1.read_list()
        
        