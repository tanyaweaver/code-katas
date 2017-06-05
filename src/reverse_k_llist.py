class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist(object):
    def __init__(self, iter=None):
        self.head = None
        if iter:
            for _ in iter:
                self.add(_)

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def reverse_k_elements(self, k):
        cur = self.head
        counter, round_ = 0, 0
        prev_last = None
        group_first = self.head
        while cur and isinstance(k, int) and k > 0:
            while cur.next and counter < k - 1:
                node_to_move = cur.next
                cur.next = cur.next.next
                node_to_move.next = group_first
                group_first = node_to_move
                counter += 1
                if round_ == 0:
                    self.head = group_first
                else:
                    prev_last.next = group_first
            if cur.next:
                round_ += 1
                counter = 0
                prev_last = cur
                cur = cur.next
                group_first = cur
            else:
                break

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        self.head = prev
