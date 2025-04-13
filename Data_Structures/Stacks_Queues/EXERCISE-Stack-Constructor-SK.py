# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
class Stack:
    def __init__(self, value):
        new_node = Node(value) # Create a new node with the given value
        self.top = new_node # Top of the stack is the new node
        #self.bottom = new_node # Not needed in stack implementation as we only need to keep track of the top node
        #self.next = None # Not needed in stack implementation as we only need to keep track of the top node
        self.height = 1 # Height of the stack is 1 when we add the first node




my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""