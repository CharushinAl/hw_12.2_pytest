from utils.dicts import get_val

import pytest

test_dict = {1: '11', 2: '22', 3: '33'}

def test_get_val():
    assert get_val(test_dict, 2) == '22'
    assert get_val(test_dict, 2, '44') == '22'
    assert get_val(test_dict, 4, '44') == '44'
    assert get_val({}, 2) == 'git'


def test_get1(dictionary_fixture):
    assert get_val(dictionary_fixture, 2) == '22'


def test_get2(dictionary_fixture):
    assert get_val(dictionary_fixture, 2, '44') == '22'


def test_get3(dictionary_fixture):
    assert get_val(dictionary_fixture, 4, '44') == '44'


def test_get4(dictionary_fixture):
    assert get_val({}, 2) == 'git'
