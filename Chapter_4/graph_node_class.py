class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.visited = False
        
    def __str__(self):
        return str((self.data, self.visited))