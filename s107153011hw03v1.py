print("By 107153011 陳鍇翰")
class Stack:
    def __init__(self, size : int):
        self._top = 0
        self._data = [None for _ in range(size)]
        
    def push(self,i : int) -> None:
        self._data[self._top] = i
        self._top += 1
        
    def pop(self) -> int:
        self._top -= 1
        return self._data[self._top]
    
    def cal(self):
        self._top = 0
        store = input("輸入正確的後置表示式進行計算:")
        
        for _ in store:
            if _ == "+":
                self.push(float(self.pop())+float(self.pop()))
            elif _ == "-":
                cache = Stack(2)
                cache.push(self.pop())
                cache.push(self.pop())
                self.push(float(cache.pop())-float(cache.pop()))
            elif _ == "*":
                self.push(float(self.pop())*float(self.pop()))              
            elif _ == "/":
                cache = Stack(2)
                cache.push(self.pop())
                cache.push(self.pop())
                self.push(float(cache.pop())/float(cache.pop()))                
            else:
                self.push(_)
        print(self.pop())

if __name__ == "__main__":
    storage = Stack(50)
    storage.cal()
