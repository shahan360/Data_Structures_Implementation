def pop(self):
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while(temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None 
    self.length -= 1
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp

my_linked_list = LinkedList(10)
my_linked_list.append(5)

my_linked_list.print_list()