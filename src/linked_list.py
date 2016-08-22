#!/usr/bin/env python
# -*- coding: utf -8 -*-
#from __future__ import unicode_literals


class Node(object):
    def __init__(self, value):
        """Create an instance of Node."""
        self.value = value
        self.next_node = None


class LinkedList(object):
    def __init__(self, param=None):
        """Create an instance of LinkedList.
            The optional parameter needs to be an itarable."""
        self.head_node = None
        self.length_list = 0
        try:
            param = param.decode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            pass
        if hasattr(param, '__iter__'):
            for i in param:
                self.push(i)
        elif param:
            self.push(param)

    def push(self, val):
        """Insert a new node to the head of a linked list."""
        try:
            val = val.decode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            pass
        new_node = Node(val)
        new_node.next_node = self.head_node
        self.head_node = new_node
        self.length_list += 1
        return self.head_node

    def __len__(self):
        """Return the length of the linked list for the built-in len."""
        return self.length_list

    def size(self):
        """Return the length of the linked list."""
        return len(self)

    def search(self, val):
        """Search for a node based on the val."""
        try:
            val = val.decode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            pass
        current_node = self.head_node
        flag = True
        while current_node and flag:
            if current_node.value != val:
                current_node = current_node.next_node
            else:
                flag = False
        return current_node

    def remove(self, val):
        """Remove a node from linked list."""
        try:
            val = val.decode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            pass
        current_node = self.head_node
        previous_node = None
        while current_node:
            if current_node.value == val:
                if not previous_node:
                    self.head_node = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
                self.length_list -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        return False

    def pop(self):
        """Remove a node from the head, return removed node value."""
        if self.length_list == 0:
            raise AttributeError('empty list')
        popped_node = self.head_node
        self.head_node = self.head_node.next_node
        self.length_list -= 1
        return popped_node

    def display(self):
        """Display a linked list as a tuple."""
        current_node = self.head_node
        display_tuple = '(' if current_node is not None else '()'
        while current_node:
            if not current_node.next_node:
                display_tuple += str(current_node.value) + ')'
            else:
                display_tuple += str(current_node.value) + ', '
            current_node = current_node.next_node
        return display_tuple
