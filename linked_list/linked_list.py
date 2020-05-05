class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    # add a node at the end
    def add_node(self, node):
        if self.head:
            current = self.head
            while current.next: current = current.next
            current.next = node
        else: self.head = node
        self.len += 1

    def get_at_pos(self, pos):
        counter = 1
        if pos < 1: return None
        current = self.head
        while current and counter <= pos:
            if counter == pos: return current
            current = current.next
            counter += 1
        return None
    
    def insert_at_pos(self, node, pos):
        counter = 1
        if pos == 1: # at the head
            node.next = self.head
            self.head = node
        else: 
            current = self.head
            while current and counter < pos:
                counter += 1
                if pos == counter:
                    node.next = current.next
                    current.next = node
                current = current.next
        self.len += 1

    def del_by_val(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if current.value == value: 
            if prev: prev.next = current.next
            else: self.head = current.next
        self.len -= 1

    def del_by_pos(self, pos):
        if pos == 1: 
            self.head = self.head.next
            return 
        current = self.head
        counter = 1
        while current and counter < pos: 
            counter += 1
            if counter == pos: 
                current.next = current.next if not current.next else current.next.next                
            current = current.next
        self.len -= 1

    def print_it(self):
        s = []
        current = self.head
        while current: 
            s.append(f"[{current.value}]")
            current = current.next
        print('-->'.join(s))

    def reverse_iterative(self):
        nxt = None
        current = self.head
        prev = None
        while current: 
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev





# Test cases
# Set up some Nodes
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.add_node(e2)
ll.add_node(e3)
ll.print_it()
# Test get_at_pos
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_at_pos(3).value)

# Test insert_at_pos
ll.insert_at_pos(e4,3)
# Should print 4 now
print(ll.get_at_pos(3).value)
ll.print_it()
# Test delete
ll.del_by_val(1)
# Should print 2 now
print(ll.get_at_pos(1).value)
# Should print 4 now
print(ll.get_at_pos(2).value)
# Should print 3 now
print(ll.get_at_pos(3).value)

print(f"len = {ll.len}")
# ll.del_by_pos(1)
ll.del_by_pos(3)
print(ll.get_at_pos(1).value)
print(ll.get_at_pos(2).value)
# print(ll.get_at_pos(1).value)

ll.print_it()

ll.reverse_iterative()
ll.print_it()

ll.add_node(Node(1))
ll.add_node(Node(9))
ll.add_node(Node(8))
ll.add_node(Node(90))

ll.print_it()

ll.reverse_iterative()
ll.print_it()