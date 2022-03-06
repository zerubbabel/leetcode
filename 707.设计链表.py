#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start

class MyLinkedList:

    def __init__(self):
        self.a=[]
        self.head=-1
        self.n=0

    def get(self, index: int) -> int:
        if index<0 or index>=self.n:return -1
        if index==0:return self.a[self.head][0]
        k=0
        cur=self.head
        while k<index and cur!=-1:
            k+=1
            cur=self.a[cur][1]
        return self.a[cur][0]

    def addAtHead(self, val: int) -> None:
        self.a.append([val,self.head])
        self.head=self.n
        self.n+=1

    def addAtTail(self, val: int) -> None:
        self.a.append([val,-1])
        if self.n==0:
            self.head=0
            return
        
        cur=self.head
        while self.a[cur][1]!=-1:
            cur=self.a[cur][1]
        self.a[cur][1]=self.n
        self.n+=1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0:
            self.a.append([val,self.head])
            self.head=self.n
            self.n+=1
        elif index>=self.n:
            return 
        else:
            prev,cur,k=-1,self.head,0
            while k<index:
                prev,cur=cur,self.a[cur][1]
                k+=1
            self.a.append([val,cur])
            if prev==-1:
                self.head=self.n
            else:
                self.a[prev][1]=self.n
            self.n+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.n:return
        if index==0:
            self.head=self.a[self.head][1]
            self.n-=1
        else:
            k,prev,cur=0,-1,self.head
            while k<index:
                k+=1
                prev,cur=cur,self.a[cur][1]
            self.a[prev][1]=self.a[cur][1]
            self.n-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

