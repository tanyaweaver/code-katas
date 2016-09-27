# -*- coding: utf -8*-
from setuptools import setup

setup(
    name="autocomplete",
    description="Code 401 - Python assignment",
    version=0.1,
    license='MIT',
    author="Tatiana Weaver",
    author_email="email@email.com",
    py_modules=['autocomplete', 'trie'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
