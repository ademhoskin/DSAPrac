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
            temp = next.value
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def prepend:

LL1= LinkedList(7)
print(LL1.head.value)

