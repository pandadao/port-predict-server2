# port-predict
this project is to implement the paper "A new method for symmetric NAT Traversal in udp and TCP"

## The architecture
#### port-predict 資訊圖:
![Alt text](https://github.com/pandadao/port-predict/blob/master/figure/port%20predict%20paper%20implement.jpg)

#### 程式架構及區塊TP-connect 註冊流程圖

![Alt text](https://github.com/pandadao/port-predict/blob/master/figure/%E7%A8%8B%E5%BC%8F%E6%9E%B6%E6%A7%8B%E5%8F%8A%E5%8D%80%E5%A1%8ATP-connect%20%E8%A8%BB%E5%86%8A.jpg)

#### 程式架構及區塊 TP-connect 連線流程圖:
![Alt text](https://github.com/pandadao/port-predict/blob/master/figure/%E7%A8%8B%E5%BC%8F%E6%9E%B6%E6%A7%8B%E5%8F%8A%E5%8D%80%E5%A1%8ATP-connect%E9%80%A3%E7%B7%9A.jpg)



## How to use
目前完成了第1部份client可以連上server1得到自己的IP和port, server1部份可以不停的監聽連入資訊並且展示連入的socket資訊 <br />

> python server1-portget.py 

> python TP-connect.py


你將可以比對client和server1所接收到的IP和port資訊是否一致
<br/>

機器連上後,得到的ID值不變,變且要隨時與server2保持連線,當進行過一次連線後ID一樣保持不變,但是密碼要變.
