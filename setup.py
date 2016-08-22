# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='parenthetics',
    description='proper parenthetics exersice for Code401-python',
    version=0.1,
    author='Tatiana Weaver',
    author_email='email@email.com',
    license='MIT',
    py_modules=['parenthetics', 'linked_list', 'stack'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
