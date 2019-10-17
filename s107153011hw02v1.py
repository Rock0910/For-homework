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
        self._data = []
        self._top = 0
        
    def isEmpty(self):
        if len(self._data) == 0:
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
        
    print()
    dump(data1)
    print()
    print("\n------------------------------------------------------------------\n")
    print("偷看(peep)其中元素為多少")
    for i in range(9):
        print(f"陣列中位於 {i} 位置的元素的數值是: ",end = "")
        data1.peep(i)
    print("\n------------------------------------------------------------------\n")
    print("將數字彈 (pop) 出堆疊裡")
    for i in range(1,10):
        print(f"彈出 {data1.pop()} ;",end = "")
                    
        dump(data1)
    print("\n------------------------------------------------------------------\n")
    print("查看top為多少")
    print(data1.top)
    
    print("\n檢查堆疊是否為空的")
    data1.isEmpty()
    print("\n堆疊現在內容")
    dump(data1)
    print("\n------------------------------------------------------------------\n")
    print("清空/刪除 堆疊...")
    data1.empty()
    print("\n堆疊現在內容")
    print(data1._data,"top 在",data1.top)
    
    print("\n檢查堆疊是否為空的")
    data1.isEmpty()
    print("\n------------------------------------------------------------------\n")
    print("後語:\n@property 用法還不是很清楚\n且要是在 pop 後 peep \
          \n\n他還是會顯示出相同內容\n跟老師說的看不到就好有點不一樣\
          \n要是使用者想要 pop 後檢查全部他還是能看到內容\
          \n雖說通常不會給使用者這樣做就是了\
          \n\n以及清空堆疊內容的定義 是直接覆蓋掉成空列表 還是空間保存下來 裡面取代成None?\
          \n後者的話 isEmpty 要怎麼檢查是否為空的就又要花時間寫了\
          \n目前是以前者 直接覆蓋掉成空列表的狀態 讓empty相關變簡單很多\
          \n\n\t\t\t\tby 107153011 陳鍇翰")
    input("按下Enter鍵結束本程式:")
    