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
            
#------------------------------------------------------------------------------
if __name__ == "__main__":
    Test = queue(10)
    for i in range(12):
        Test.enqueue(i)
        
    Test.check()
    
    for i in range(4):
        Test.dequeue()
        
    Test.check()
    
    for i in range(8,15):
        Test.enqueue(i)
        
    Test.check()
