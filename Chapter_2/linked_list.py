from node_class import node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self,data):
        n = node(data)
        n.next = self.head
        self.head = n
        self.size += 1
    def append(self,data):
        if self.head is None:
            self.head = node(data)
        else:
            n = node(data)
            n.next = None
            nodes = self.head
            while nodes.next is not None:
                nodes = nodes.next
            nodes.next = n
        self.size +=1
    def __len__(self):
        return self.size
    
    def __str__(self):
        node = self.head
        result = ''
        while node:
            value = node.data
            node = node.next
            result += '->'+str(value)
        return result