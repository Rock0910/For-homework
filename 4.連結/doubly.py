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
        else:
            cur.next.prev = cur.prev
            
        if cur.next:
            cur.next = cur.next.next
            
"""
移除一個Node
找到Node
將Node的next拿去覆蓋上一個的next
把新導向的prev改成Node 的上一個
"""
    
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
    text = "Braindamaged"
    head = doubly(text[0])
    
    for i in text[1:]:
        head.append(doubly(i))
        
    dump(head)
    print()
    print()
    
    print("移除 r ")
    head.remove("r")
    dump(head)
    print()
    print()
    rdump(head)
    
    
    
