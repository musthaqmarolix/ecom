# inorder --- > starrting from node, then left then node then right

# preorder -- >root>left of root> right of root

# post0 -- >left>right>root


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        print(str(root.val)+"-->", end = "") # printing the root
        inorder(root.left) # traversing through left recursively
        inorder(root.right) # traversing through right recursively

def preorder(root):
    if root:
        preorder(root.left) # traversing through left recursively
        print(str(root.val)+"-->", end = "") # printing the root
        preorder(root.right) # traversing through right recursively

def postorder(root):
    if root:
        postorder(root.left) # traversing through left recursively
        postorder(root.right) # traversing through right recursively
        print(str(root.val)+"-->", end = "") # printing the root
        

root = Node("A")

#right side 

root.right = Node("G")
root.right.left = Node("F")
root.right.right = Node("H")
root.right.right.left = Node("I")

# left side
root.left = Node("B")
root.left.left = Node("C")
root.left.right = Node("E")
root.left.left.right = Node("D")

#inorder(root)
postorder(root)


fruits=["a","b","c"]
new_fruits=[x.replace("c","d")for x in fruits]
print(new_fruits)