# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='flight-paths',
    description='flight path exersice for Code401-python',
    version=0.1,
    author='Tatiana Weaver',
    author_email='email@email.com',
    license='MIT',
    py_modules=['flight_paths', 'graph'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
