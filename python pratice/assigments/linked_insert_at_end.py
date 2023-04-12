class node:
   def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
   def __init__(self):
      self.head=None
    
   def insertatend(self,newdata):
      newdata=node(newdata)
      if self.head == None:
         self.head=newdata
         return
      else:
         last=self.head
      while(last.next is not None):   # if i have something after H
            last = last.next
      last.next = newdata

   def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

linked_list =linkedlist()
linked_list.head = node("gun")
second = node("bun")
third = node("men")

linked_list.head.next = second
second.next = third

#linked_list.insertatend("when")

#linked_list.display()