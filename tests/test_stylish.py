#!usr/bin/env python3


from gendiff.formats.stylish import (
    make_stylish_represent, style_value
)
from gendiff.formats.plain import sort_data
from gendiff.decoder import decode


CHANGED = {'change_key': ['changed', ('value1', 'value2')]}
ADDED = {'add_key': ['added', 'add_val']}
REMOVED = {'remove_key': ['removed', 'rmv_val']}
UNCHANGED = {'key': ['unchanged', 'value']}


def test_decode():
    assert 'patata' == decode('patata')
    assert 'null' == decode(None)
    assert 'false' == decode(False)
    assert 'true' == decode(True)
    assert '12' == decode(12)


def test_make_make_stylish_represent():
    data = {**CHANGED, **ADDED, **REMOVED, **UNCHANGED}
    sorted_data = sort_data(data)
    expected_data = '{\n  + add_key: add_val\n  - change_key: value1\n  + change_key: value2\n    key: value\n  - remove_key: rmv_val\n}'  # noqa: E501

    assert expected_data == make_stylish_represent(sorted_data)


def test_style_value():
    value = {'key': 'value'}
    nested_value = {'key': {'another key': 42}}
    expected_for_val = '{\n        key: value\n    }'
    expected_nested_val = '{\n        key: {\n            another key: 42\n        }\n    }'

    assert expected_for_val == style_value(value, nest_lvl=0)
    assert expected_nested_val == style_value(nested_value, nest_lvl=0)
