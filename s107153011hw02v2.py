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
       
    @property
    def top(self) -> int:
        return self._top
   
    def peep(self, i : int) -> int:
        print(self._data[i])
        
    def empty(self) -> None:
        self._top = 0
        
    def isEmpty(self):
        if self._top == 0:
            print("True")
        else:
            print("False")
        
def dump(data1):
    print("堆疊內容 : [",end = "")
    
    for i in range(data1._top):
        print(f" {data1._data[i]}",end = "")
        
    print(f" ] , top = {data1.top}")
#-----------------------------------------------
if __name__ == "__main__":
    print("設定堆疊大小")
    data1 = Stack(9)
    print("\n堆疊現在狀況")
    print(data1._data)
    print("\n------------------------------------------------------------------\n")
    print("將數字放 (push) 進堆疊裡")
    for i in range(1,10):
        print(f"放入 {i} 到陣列;",end = "")
        
        data1.push(i)
        
        dump(data1)
    print("\n------------------------------------------------------------------")
    print()
    dump(data1)
    print()
    print("------------------------------------------------------------------\n")
    print("偷看(peep)其中元素為多少")
    for i in range(9):
        print(f"陣列中位於 {i} 位置的元素的數值是: ",end = "")
        data1.peep(i)
    print("\n------------------------------------------------------------------\n")
    print("**檢查堆疊是否為空的**")
    data1.isEmpty()
    print("\n------------------------------------------------------------------\n")
    print("將數字彈 (pop) 出堆疊裡")
    for i in range(data1._top):
        print(f"彈出 {data1.pop()} ;",end = "")
                    
        dump(data1)
    print("\n------------------------------------------------------------------\n")
    print("查看top為多少")
    print(data1.top)
    print("\n------------------------------------------------------------------\n")
    print("堆疊現在內容")
    dump(data1)
    print("\n執行 清空堆疊(empty)...")
    data1.empty()
    print("\n------------------------------------------------------------------\n")
    print("**檢查堆疊是否為空的**")
    data1.isEmpty()
    print("\n------------------------------------------------------------------\n")
    print("後語:\n@property 用法還不是很清楚\n這次將大部分功能都用_top來定義\n相比上一版簡單很多 且在使用者端看起來不會矛盾\
          \n\n\t\t\t\tby 107153011 陳鍇翰")
    input("按下Enter鍵結束本程式:")
    
