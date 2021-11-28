from csv import writer

class Node:
    def __init__(self,data,nama):
        self.data=data
        self.nama=nama
        self.next=None 
class linked_list:
    def __init__(self):
        self.start=None
       
    def insert(self,data,nama):
        newnode=Node(data,nama)
        if self.start==None:
            self.start=newnode
        else:
            ptr=self.start 
            while(ptr.next is not None):
                ptr=ptr.next 
            ptr.next=newnode
    def printll(self):
        ptr=self.start
        if(ptr is None):
            print("None")
        else:
            while(ptr!=None):
                print(ptr.nama,"-->",end=" ")
                ptr=ptr.next
            print("None")  
              
            
class hash:
    def __init__(self):
        self.size=5
        self.hastable=list()
        for x in range(self.size):
            self.hastable.append(linked_list())
    def has(self,key):
        return key%5
    def insert_key(self,key,nama):
        index=self.has(key)
        self.hastable[index].insert(key,nama)
    def print(self):
        print("Index\t\tValue\n")
        for x in range(self.size):
            print(x,end="\t\t")
            self.hastable[x].printll()
   
ht=hash() 
ulangi='y'
while(ulangi=='y'): 
  with open("Kamus.csv","a",newline='') as kamus:   
    counter=0
    kata=input(str("Masukkan kata: "))
    writer_objek=writer(kamus)
    writer_objek.writerow(kata)
    for i in kata:
        ascii=ord(i)
        counter=counter+ascii
    nilai=counter
    ht.insert_key(nilai,kata)

    ulangi=input("Ingin mengulang?(y/t): ")
ht.print()


  
            


    

        
        