#linkedlist inerted at the starting

class node():
   def __init__(self,data):                                               
      self.data=data
      self.next=None 

class linkedlist:
   def __init__(self):
      self.head=None  

   def insertstartat(self,newdata):
      newdata=node(newdata)
      newdata.next=self.head
      self.head=newdata

      

   def display(self):
      temp=self.head
      while temp is not None:
        print(temp.data)
        temp=temp.next  

l=linkedlist()             
l.head=node("ram")                     
second=node("raj")
third=node("rani")

l.head.next=second
second.next=third
#l.insertstartat("jonny")
# l.display()

