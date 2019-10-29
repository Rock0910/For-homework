"""
宣告一個類別 (class) 稱為 Node
Node 有兩個欄位：
    data：資料欄位；存放資料用。為簡單起見，可以單純是一個整數 (int)。
    next：指標欄位；指向下一個節點。它的型別就是 Node 本身。
新增節點 (addNode)：
    分配空間：node = new Node()
    找到串列最後一個元素，假設稱為 last
    接上串列：last.next = node
移除節點 (removeNode)：？
"""
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    def addNode(self, new):
        new = Node(new)
        self._next = new
        
    def removeNode(self):
        self._next = None
        
class pointer:
    def __init__(self):
        self._head = None
        self._tail = None
    
        
#---------------------------------------
init = pointer()
example = "Something"

for x in example:
    init.addNode(x)
    
print(init)