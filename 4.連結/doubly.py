class doubly():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
    def append(self,node):
        cur = self
        while cur.next:
            cur.next.prev = cur
            cur = cur.next
        
        cur.next = node
        
    def remove(self,char):
        cur = self
        while cur.next and cur.next.data != char:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
            
        #if cur.prev.data == char:
         #   cur.prev = cur.prev.prev
            
            
    def insert(self,behind,insert):
        cur = self
        while cur:
            if cur.next is None and cur.data == behind:
                self.append(doubly(insert))
            elif cur.data == behind:
                new_node = doubly(insert)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next
            
    
def dump(linked):
    cur = linked
    while cur:
        print(f"-> {cur.data}",end = "")
        cur = cur.next

def rdump(linked):
    cur = linked.next
    
    while cur.prev:        
        print(f"-> {cur.prev.data}",end = "")
        print(cur.data,end = "")
        cur = cur.next
       
#-----------------------------------------
if __name__ == "__main__":
    text = "123456789"
    head = doubly(text[0])
    
    for i in text[1:]:
        head.append(doubly(i))
        
    dump(head)
    print()
    print()
    
    print("移除 5 ")
    head.remove("5")
    dump(head)
    print()
    print()
    
    print("在 1 後面插入 x")
    head.insert("1","x")
    dump(head)
    
    
    
