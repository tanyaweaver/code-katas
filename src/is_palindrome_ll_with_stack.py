from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    def add_node(self, x):
        cur = self
        while cur.next:
            cur = cur.next
        cur.next = ListNode(x)

    def print_list(self):
        list_values = []
        cur = self
        while cur is not None:
            list_values.append(cur.value)
            cur = cur.next
        return list_values

    def find_length(self):
        length = 0
        cur = self
        while cur:
            length += 1
            cur = cur.next
        return length

    def is_palindrome(self):
        stack = deque()
        length = self.find_length()
        cur = self
        for i in range((length)/2):
            stack.append(cur.value)
            cur = cur.next
        if length % 2 != 0:
            cur = cur.next
        while cur:
            if cur.value == stack.pop():
                cur = cur.next
            else:
                return False
        return True
