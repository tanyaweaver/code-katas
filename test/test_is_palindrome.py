from src.isPalindromeLinkedList import Node, LinkedList


def test_ll1():
    ll = LinkedList()
    assert ll.print_list() == []


def test_ll2():
    ll = LinkedList()
    ll.add_node_front(1)
    assert ll.print_list() == [1]


def test_ll3():
    ll = LinkedList()
    result = [1, 3, 5, 7]
    for x in result:
        ll.add_node_end(x)
    assert ll.print_list() == result


def test_ll4():
    ll = LinkedList()
    result = [1, 3, 5, 7]
    for x in result:
        ll.add_node_front(x)
    assert ll.print_list() == [7, 5, 3, 1]


def test_ll5():
    ll = LinkedList()
    result = [1, 3, 5, 7]
    for x in result:
        ll.add_node_end(x)
    ll.delete_node(7)
    assert ll.print_list() == [1, 3, 5]


def test_ll6():
    ll = LinkedList()
    result = [1, 3, 5, 7]
    for x in result:
        ll.add_node_end(x)
    ll.delete_node(1)
    assert ll.print_list() == [3, 5, 7]


def test_ll7():
    ll = LinkedList()
    result = [1, 3, 1, 7]
    for x in result:
        ll.add_node_end(x)
    ll.delete_node(1)
    assert ll.print_list() == [3, 7]


def test_ll8():
    ll = LinkedList()
    result = [1, 3, 5, 7]
    for x in result:
        ll.add_node_end(x)
    ll.delete_node(71)
    assert ll.print_list() == [1, 3, 5, 7]


def test_ll9():
    ll = LinkedList()
    result = [1, 3, 1, 7]
    for x in result:
        ll.add_node_end(x)
    ll.delete_node(1)
    assert ll.head.value == 3


def test_find_length1():
        ll = LinkedList()
        result = [1, 3, 2, 7]
        for x in result:
            ll.add_node_end(x)
        assert ll.find_length() == 4


def test_split_in_half1():
        ll = LinkedList()
        result = [1, 3, 2, 7]
        for x in result:
            ll.add_node_end(x)
        ll, list_2 = ll.split_in_half()
        assert ll.print_list() == [1, 3]


def test_split_in_half2():
        ll = LinkedList()
        result = [1, 3, 2, 7]
        for x in result:
            ll.add_node_end(x)
        ll, list_2 = ll.split_in_half()
        assert list_2.print_list() == [2, 7]


def test_split_in_half3():
        ll = LinkedList()
        result = [1, 3, 2, 7, 5]
        for x in result:
            ll.add_node_end(x)
        ll, list_2 = ll.split_in_half()
        assert ll.print_list() == [1, 3, 2]


def test_split_in_half4():
        ll = LinkedList()
        result = [1, 3, 2, 7, 5]
        for x in result:
            ll.add_node_end(x)
        ll, list_2 = ll.split_in_half()
        assert list_2.print_list() == [7, 5]


def test_split_in_half5():
        ll = LinkedList()
        ll, list_2 = ll.split_in_half()
        assert list_2 is None


def test_split_in_half6():
        ll = LinkedList()
        ll, list_2 = ll.split_in_half()
        assert ll.print_list() == []


def test_split_in_half7():
        ll = LinkedList()
        ll.add_node_end(1)
        ll, list_2 = ll.split_in_half()
        assert list_2.head is None


def test_split_in_half8():
        ll = LinkedList()
        ll.add_node_end(1)
        ll, list_2 = ll.split_in_half()
        assert ll.print_list() == [1]


def test_split_in_half9():
        ll = LinkedList()
        ll.add_node_end(1)
        ll.add_node_end(2)
        ll, list_2 = ll.split_in_half()
        assert ll.print_list() == [1]


def test_split_in_half10():
        ll = LinkedList()
        ll.add_node_end(1)
        ll.add_node_end(2)
        ll, list_2 = ll.split_in_half()
        assert list_2.print_list() == [2]


def test_reverse_list1():
        ll = LinkedList()
        result = [1, 3, 2, 7, 5]
        for x in result:
            ll.add_node_end(x)
        ll.reverse_list()
        assert ll.print_list() == [5, 7, 2, 3, 1]


def test_reverse_list2():
    ll = LinkedList()
    ll.reverse_list()
    assert ll.print_list() == []


def test_is_palindrome1():
    ll = LinkedList()
    result = [1, 3, 2, 7, 5]
    for x in result:
        ll.add_node_end(x)
    assert ll.is_palindrome() is False


def test_is_palindrome2():
    ll = LinkedList()
    result = [1, 3, 2, 3, 1]
    for x in result:
        ll.add_node_end(x)
    assert ll.is_palindrome() is True


def test_is_palindrome3():
    ll = LinkedList()
    result = [1, 3, 3, 1]
    for x in result:
        ll.add_node_end(x)
    assert ll.is_palindrome() is True


def test_is_palindrome4():
    ll = LinkedList()
    assert ll.is_palindrome() is True
