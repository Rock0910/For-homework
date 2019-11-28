print("107153011陳鍇翰")

class queue:
    def __init__(self,size):
        self._data = [None for _ in range(size)]
        self._head = -1
        self._tail = 0
    
    def dequeue(self):
        if self._head +1 % len(self._data) == self._tail % len(self._data):
            print("佇列已經空了")
        else:
            self._head += 1
            
    def enqueue(self,target):
        if self._tail % len(self._data) == self._head % len(self._data):
            print("佇列已滿")
        else:
            self._data[self._tail % len(self._data)] = target
            self._tail += 1
    
    def check(self):
        print()
        for i in range(len(self._data)):
            print(self._data[i])
        
        print(f"Head {self._head},Tail {self._tail}")
        print()
            
class linkedqueue:
    def __init__(self,item):
        self._data = item
        self._next = None
    
    def dequeue(self):
        if self._next:
            self._data = self._next._data
            self._next = self._next._next
        else:
            print("已經沒東西了")
        
    def enqueue(self,target):
        cur = self
        while cur._next:
            cur = cur._next
            
        cur._next = linkedqueue(target)

def dump(linked):
    cur = linked
    while cur:
        print(f"-> {cur._data}",end = "")
        cur = cur._next
#------------------------------------------------------------------------------
if __name__ == "__main__":
    Test = queue(10)
    print("----------------------------------------------------\nenqueue中...\n")
    for i in range(12):
        Test.enqueue(i)
    
    Test.check()
    
    print("----------------------------------------------------\ndequeue中...\n")
    for i in range(4):
        Test.dequeue()
        
    Test.check()
    print("Head在3 dequeue成功\n----------------------------------------------------")
    
    print("再次enqueue新數字\n")
    for i in range(8,15):
        Test.enqueue(i)
        
    Test.check()
    print("完成")
    
    
    print("----------------------------------------------------\n測試Linkedqueue")
    print("enqueue中...\n")
    x = linkedqueue("a")
    
    x.enqueue("b")
    x.enqueue("c")
    
    dump(x)
    print("\n\ndequeue")
    x.dequeue()
    print()
    dump(x)
    print("\n\n完成\n----------------------------------------------------")
