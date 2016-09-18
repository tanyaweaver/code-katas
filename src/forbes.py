#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
import json


with open('assets/forbes_billionaires_2016.json') as data_file:
    DATA = json.load(data_file)
print(DATA)
