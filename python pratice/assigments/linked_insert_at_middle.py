class node:
   def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
   def __init__(self):
      self.head=None
   def inseratatmiddle(self,middlenode,newdata):
      if middlenode is  None:
         print('mainted node is node')
         return
      newnode=node(newdata)
      newnode.next=middlenode.next
      middlenode.next=newnode
   def display(self):
      temp=self.head
      while temp is not None:
         print(temp.data)
         temp=temp.next
