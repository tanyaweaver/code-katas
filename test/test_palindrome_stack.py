from src.is_palindrome_ll_with_stack import ListNode


def test_list_node1():
    ll = ListNode(5)
    assert ll.value == 5


def test_list_node2():
    ll = ListNode(5)
    values = [1, 2, 3, 4]
    for x in values:
        ll.add_node(x)
    assert ll.print_list() == [5, 1, 2, 3, 4]


def test_list_length1():
    ll = ListNode(5)
    values = [1, 2, 3, 4]
    for x in values:
        ll.add_node(x)
    assert ll.find_length() == 5


def test_is_palindrome1():
    ll = ListNode(5)
    values = [1, 2, 3, 4]
    for x in values:
        ll.add_node(x)
    assert ll.is_palindrome() is False


def test_is_palindrome2():
    ll = ListNode(5)
    values = [1, 2, 2, 1, 5]
    for x in values:
        ll.add_node(x)
    assert ll.is_palindrome() is True


def test_is_palindrome3():
    ll = ListNode(5)
    values = [1, 2, 1, 5]
    for x in values:
        ll.add_node(x)
    assert ll.is_palindrome() is True
