class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def print_list(self):
        list_values = []
        cur = self.head
        while cur is not None:
            list_values.append(cur.value)
            cur = cur.next
        return list_values

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
            if cur.next.value == x:
                cur.next = cur.next.next
                self.length -= 1
            else:
                cur = cur.next

    def find_length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def split_in_half(self):
        length = self.find_length()
        list_2 = None
        if length > 0:
            cur = self.head
            for i in range((length - 1)/2):
                cur = cur.next
            list_2 = LinkedList()
            list_2.head = cur.next
            cur.next = None
        return self, list_2

    def reverse_list(self):
        cur = self.head
        if cur is not None:
            while cur.next:
                node_to_move = cur.next
                cur.next = node_to_move.next
                node_to_move.next = self.head
                self.head = node_to_move

    def is_palindrome(self):
        self, list_2 = self.split_in_half()
        if list_2:
            list_2.reverse_list()
            cur1 = self.head
            cur2 = list_2.head
            while True:
                if cur2 is None:
                    return True
                if cur1.value != cur2.value:
                    return False
                else:
                    cur1 = cur1.next
                    cur2 = cur2.next
        else:
            return True
