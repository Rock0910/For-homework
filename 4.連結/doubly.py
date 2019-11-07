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
        
        while cur:
            if cur.data == char:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
            
        """        
        while cur.next and cur.next.data != char:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
        """    
            
            
    def insert(self,behind,insert):
        cur = self
        while cur:
            if cur.next is None and cur.data == behind:
                self.append(doubly(insert))
            elif cur.data == behind:
                new_node = doubly(insert)
                #先建立新的Node
                nxt = cur.next
                #為了要讓新的Node能連上將要移除的next先存
                cur.next = new_node
                #將cur的next設定成剛建立的node
                new_node.next = nxt
                new_node.prev = cur
                #把new_node的next跟prev都設定好
                
                nxt.prev = new_node
                #再把new_node下一個的prev指向自己
            cur = cur.next
            #要是cur不符合上面敘述 指針移動
            
    
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
    
    
    
