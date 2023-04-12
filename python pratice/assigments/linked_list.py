class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def AddAtStart(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def deletion(self, removeKey):
        head = self.head
        if head:
            if head.data == removeKey:
                self.head = head.nexthead = None
                return
            
            while head is not None:
                if head.data == removeKey:
                    break
                prev = head
                head = head.next

            if head == None:
                return
            
            prev.next = head.next
            head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data )
            temp = temp.next

linked_list = LinkedList()
linked_list.AddAtStart("july")
linked_list.AddAtStart("june")
linked_list.AddAtStart("may")
linked_list.AddAtStart("apr")
linked_list.AddAtStart("mar")
linked_list.AddAtStart("feb")
linked_list.AddAtStart("jan")

#print("linked list before deletion: ")
#linked_list.display()

#linked_list.deletion("apr")

#print("linked list after deletion: ")
#linked_list.display()