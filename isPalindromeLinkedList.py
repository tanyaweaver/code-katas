class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node_front(self, x):
        new_head = Node(x)
        new_head.next = self.head
        self.head = new_head
        self.length += 1

    def add_node_end(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(x)
        self.length += 1

    def delete_node(self, x):
        if self.head is None:
            return None
        cur = self.head
        if cur.value == x:
            self.head = cur.next
        while cur.next is not None:
            if cur.next.val == x:
                cur.next = cur.next.next
            else:
                cur = cur.next
