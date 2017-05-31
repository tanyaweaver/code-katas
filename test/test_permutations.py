import pytest
from src.str_permutations import helper_perm, str_permutation


def test_helper_perm1():
    all_perm = set()
    assert helper_perm('abc', 2, all_perm) == set(['abc'])


def test_helper_perm2():
    all_perm = set()
    assert helper_perm('abc', 1, all_perm) == set(['abc', 'acb'])


def test_helper_perm3():
    all_perm = set()
    result = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert helper_perm('abc', 0, all_perm) == result


def test_helper_perm4():
    all_perm = set()
    assert helper_perm('', 1, all_perm) == set([])


def test_helper_perm5():
    all_perm = set()
    assert helper_perm(None, 1, all_perm) == set([])


def test_str_permutation1():
    result = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert str_permutation('abc') == result


def test_str_permutation2():
    assert str_permutation('') == []


def test_str_permutation3():
    assert str_permutation(None) == []
