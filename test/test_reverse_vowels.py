from src.reverse_vowels import reverse_vowels_of_string


def test_reverse1():
    string = 'hello, world'
    assert reverse_vowels_of_string(string) == 'hollo, werld'


def test_reverse2():
    string = 'sdrtn'
    assert reverse_vowels_of_string(string) == string


def test_reverse3():
    string = 'a a'
    assert reverse_vowels_of_string(string) == string


def test_reverse4():
    string = ',.'
    assert reverse_vowels_of_string(string) == string


def test_reverse5():
    string = None
    assert reverse_vowels_of_string(string) is None


def test_reverse6():
    string = ''
    assert reverse_vowels_of_string(string) == string
