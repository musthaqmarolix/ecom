#linked list inserted at the starting
import insert_start_at
insert_start_at.l.insertstartat("jonny")
insert_start_at.l.display()
print("inserted at the starting")

#linked list inserted at the end
import linked_insert_at_end
linked_insert_at_end.linked_list.insertatend("when")
linked_insert_at_end.linked_list.display()
print("inserted at the end")


#linked list inserted at the middle
from linked_insert_at_middle import node, linkedlist
linkedlist=linkedlist()
linkedlist.head=node('apple')
second=node('banana')
third=node('carrot')
linkedlist.head.next=second
second.next=third
linkedlist.inseratatmiddle(second,"dog")
linkedlist.display()

#linked list before and after deletion
import linked_list
print("linked list before deletion: ")
linked_list.linked_list.display()

linked_list.linked_list.deletion("apr")

print("linked list after deletion: ")
linked_list.linked_list.display()
