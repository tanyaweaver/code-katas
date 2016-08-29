# -*- encoding: utf-8 *-*
# This is an http-server#
# import pytest
# from parenthetics import parenthetics

# TABLE1 = [
#     ('(a)', 0),
#     ('(a', 1),
#     ('(a', 1),
#     ('a)', -1),
#     ('a', 0),
#     ('', None),
#     ('))))((((', -1),
#     ('(((())', 1),
#     ('(())))', -1),
#     ('()()()', 0),
# ]

# TABLE2 = [(1), (None), ([1, 2, 3]), (1.0), ({'a': 'b'}), ((1, 2))]


# @pytest.mark.parametrize('string, result', TABLE1)
# def test_parenthetics1(string, result):
#     """
#     Test whether parenthetics() returns an appropriate result
#     when string is a unicode string.
#     """
#     assert parenthetics(string) == result


# @pytest.mark.parametrize('string', TABLE2)
# def test_parenthetics2(string):
#     """
#     Test whether <TypeError> is raised when string is not
#     a unicode string.
#     """
#     with pytest.raises(TypeError):
#         parenthetics(string)
