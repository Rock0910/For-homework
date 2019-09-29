#000那邊是最後想要他產生的數字(函式也能)
print("使用python編寫")
print("建置列表中...")
number_list=[[0,0,0] for i in range(3)]
print("\n列表建置完成")
print("定義set跟get功能")
def set(x,y,z):
    #先不用append insert 似乎這邊不太適用? 已知大小append跟insert我覺得會有很多矛盾
    number_list[x][y]=z
def get(x,y):
    print(number_list[x][y])
print("\n定義成功!")
print("自動使用set函數 設定9個數字")
i,o,p=0,0,0
while p < 9:
    p+=1
    set(i,o,p)
    #抱歉 我不知道老師是不是想要手動輸入來測試 但是我暫且先寫在迴圈內讓他自己跑
    o+=1
    if o == 3:
        o=0
        i+=1
print("設定完成")
print("\n自動用get函數列出數字")
print("-----------------------------------")
q,w,e=0,0,0
while e < p:
    get(q,w)
    #抱歉 我不知道老師是不是想要手動輸入來測試 但是我暫且先寫在迴圈內讓他自己跑
    w+=1
    if w == 3:
        q+=1
        w=0
        if q == 3:
            break
print("-----------------------------------")
print("get結束")
print("\n由於函數內容無法自動顯示 所以使用print列出函數內容")
print("以下為 ```print(number_list)```的執行結果\n")
print("-----------------------------------")
print(number_list)
print("-----------------------------------")
print("\n執行結束")
print("\n\n抱歉 這邊的dump()我不太懂意思 所以我還是用print出來看看\n")
print('以下為 ```print(number_list[0],換行,number_list[1],換行,number_list[2])``` 的執行結果\n')
print("-----------------------------------")
print(number_list[0],"\n",number_list[1],"\n",number_list[2])
print("-----------------------------------")
print("\n執行結束")
print("\n\n不確定自己是否有了解老師題目 希望老師在之後可以給個範例解答 也因為看自己程式碼很爛\n")
print("<<<也請老師將程式上滾看執行狀況 抱歉>>>")
print("<<<也請看看程式碼 是否有對到題意>>>")
print("\n\n使用python編寫")
input("按下Enter鍵關閉程式:")
