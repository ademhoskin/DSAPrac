#create a Node class since all LinkedList methods make nodes
class Node(object):
    def  __init__(self, value):
        self.value = value
        self.next = None

# our datatype class
class LinkedList(Node):
    # makes new node, sets head and tail to self, and creates length of 1 since first node is made
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):

        if self.length == 0:
            return None
            self.head = None
            self.length -= 1
        pre = self.head
        temp = self.head
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
    def prepend(self, value):
        new_node = Node(VALUE)
        if self.length == 0







LL1= LinkedList(7)
LL1.append(11)
print(LL1.print_list())
LL1.pop()
print(LL1.print_list())
