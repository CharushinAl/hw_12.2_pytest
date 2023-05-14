from utils.dicts import get_val


def test_get_val():
    assert get_val({1: '11', 2: '22', 3: '33'}, 2) == '22'
    assert get_val({1: '11', 2: '22', 3: '33'}, 2, '44') == '22'
    assert get_val({1: '11', 2: '22', 3: '33'}, 4, '44') == '44'
    assert get_val({}, 2) == 'git'
