class Node(object):
    """
    Constructor to initialize the Node object.
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    """
    Constructor to initialize the List object.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            self.head = Node(val, self.head)
        self.length += 1

    def add_to_tail(self, val):
        if self.tail is None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.length += 1

    def delete_from_head(self):
        removed = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return removed

    def insert_in_sorted(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        elif self.head.val >= val:
            self.head = Node(val, self.head)
        else:
            cur = self.head
            while cur.next and cur.next.val < val:
                cur = cur.next
            cur.next = Node(val, cur.next)
            if cur.next.next is None:
                self.tail = cur.next
        self.length += 1

    def print_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


def sum_2_helper(cur1, cur2, llist):
    if not cur1.next and not cur2.next:
        sum_ = cur1.val + cur2.val
        if sum_ >= 10:
            llist.add_to_head(Node(sum_ - 10))
            llist.add_to_head(Node(1))
        return llist
    else:
        sum_ = cur1.val + cur2.val
        result = sum_2_helper(cur1.next, cur2.next, llist)
    if result.head.val == 1:
        sum_ += 1
        if sum_ >= 10:
            result.head.val = sum_ - 10
            new_head = Node(1)
            new_head.next = result.head
            result.head = new_head
        else:
            result.head.val = sum_
    else:
        new_head = Node(sum_)
        new_head.next = result.head
        result.head = new_head
    return result




def sum_2_lists(l1, l2):
    cur1 = l1.head
    cur2 = l2.head
    llist = LinkedList()
    result = sum_2_helper(cur1, cur2, llist)
    return result
