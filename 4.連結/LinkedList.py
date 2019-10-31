class Node:
    def __init__(self, data = None):
        #若不輸入資料 則存為 None
        self.data = data
        self.next = None
        
    def addNode(self,data):
        new_node = Node(data)
        self.next = data
        return new_node
    
    def removeNode(self):
        self.next = None

#--------------------------------------
init = Node()
node1 = init.addNode(1)
node2 = node1.addNode(2)
node3 = node2.addNode(3)
node4 = node3.addNode(4)

print(init.next,node1.next,node2.next,node3.next,node4.next)

node1.removeNode()

print(init.next,node1.next)

print("107153011 陳鍇翰 腦袋燒壞了\n看題目以為只設 Node 一個類別 不過翻到前面有提到 head tail\
\n而且在呼叫出內容時可能會亂 所以參考網路上的解說+實作 並自己解釋\
\n實作上跟想的概念差挺多的 老師的參考解答也讀讀看不知道能不能清楚一些\n\n\
\n下方程式碼是參考網路 自行理解加上註解 但還是不會從零開始做\
\n可以把註解符號拔掉跑下方的 但是上方的程式碼就必須加上註解或刪除")

"""
class Node:
    def __init__(self, data = None):
        #這樣可以讓data沒填入資料時設定該值為 None
        self.data = data
        self.next = None
        #先定義 Node 類別物件有什麼
        
class Link:
    def __init__(self):
        self.head = Node()
        #設定 head來儲存接下來連結的資料
        
    def addNode(self, data):
        new_node = Node(data)
        #新增一個節點 並把資料丟到 new_node 裡面        
        cur = self.head #還記得self.head跑的是 Node()嗎?
        #新增變數 cur 並讀取此物件的 head 值進去
        while cur.next != None:
            cur = cur.next        
        #要是/當 cur 的 next 不是空的 那麼把 cur 的值從 head 取代成 next 的值
        cur.next = new_node
        #然後將 cur 的 next 值取代成剛剛新增的 Node
        
    def show(self):
        store = []        
        cur_node = self.head #還記得self.head跑的是 Node()嗎?
        while cur_node.next != None: #要是 cur_node 的 next 不存在的話 就不會跑這裡了 也表示這是最後一個 Node
            cur_node = cur_node.next #還記得self.head跑的是 Node()嗎?
            store.append(cur_node.data) #append~~~
        #這部分跟上面一樣 為了讓資料存進去
        print(store)
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur=cur.next
        return total
        #以判定 next 是否存在來計算長度
    
    def removeNode(self,index): #原本是想用 self.next = None 但是這樣子後面東西全死光 跟移除"一個"而已差很多
        #但是看起來老師是想要我們只用Node來做 如果我用字串作為範例 會麻煩許多
        if index >= self.length() or index < 0:
            print("錯誤 沒有這個數字")
            return None
        cur_info = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_info +1 == index:
                last_node.next = cur_node.next #若符合 就把上一個的 next用下一個值取代
                return
            cur_info += 1        
#---------------------------------------
test = Link()
test.show()
print("\n存入9個數字")
for x in range(1,10):
    test.addNode(x)
test.show()
print("\n移除5")
test.removeNode(5)
test.show()

print("\n\n我覺得還是看老師的範例跟講解來思考好了 這個就是看別人怎麼定義來解釋而已")
for x in range(5):
    print("我還是不會 這是參考網路程式碼自己註解而已")
"""
