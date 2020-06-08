# -*- coding: utf-8 -*-
from src.util import dbutil


def test_create_query_params():
    assert dbutil.create_query_params({'name': 'hoge'}) == {'name': 'name', 'value': {'stringValue': 'hoge'}}
    # assert dbutil.create_query_params({'name': None, 'value': 1234}) == {'name': 'name', 'value': {'stringValue': 'hoge'}}
