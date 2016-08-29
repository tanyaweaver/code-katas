# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='sort-cards',
    description='sort deck of cards exersice for Code401-python',
    version=0.1,
    author='Tatiana Weaver',
    author_email='email@email.com',
    license='MIT',
    py_modules=['sort_cards', 'priority_q', 'binary_heap'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
