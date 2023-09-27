#!/usr/bin/env pyhton3

from json import dumps

statuses = {
    'added': "Property '{key}' was added with value: {value1}\n",
    'removed': "Property '{key}' was removed\n",
    'changed': "Property '{key}' was updated. From {value1} to {value2}\n"
}


def format_diff_to_plain(data):
    '''Formates raw diff in plain format'''
    string_data = make_plain_represent(data)
    return string_data[0:-1]


def make_plain_represent(  # noqa: C901
        data, key=''):
    '''Formates data in plain format'''
    string_data = ''
    for node in data:
        new_key = transform_key(node, key)
        node_type, values = data[node]
        if node_type == 'unchanged':
            continue
        elif node_type == 'nested':
            new_value = sort_data(values)
            string_line = make_plain_represent(new_value, key=new_key)
            string_data = "".join([string_data, string_line])
            continue
        added_status = statuses[node_type]
        if node_type == 'added':
            string_line = added_status.format(
                key=new_key,
                value1=transform_value(values)
            )
        elif node_type == 'removed':
            string_line = added_status.format(
                key=new_key
            )
        elif isinstance(values, tuple):
            val1, val2 = values
            string_line = added_status.format(
                key=new_key,
                value1=transform_value(val1),
                value2=transform_value(val2)
            )
        string_data = "".join([string_data, string_line])
    return string_data


def transform_value(value):
    '''Formates values'''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    return dumps(value)


def transform_key(old_key, key):
    '''Adds parent key to children'''
    if key != '':
        new_key = f'{key}.{old_key}'
    else:
        new_key = old_key
    return new_key


def sort_data(data):
    '''Sorts data'''
    keys = list(data.keys())
    keys.sort()
    sort_dict = {key: data[key] for key in keys}
    return sort_dict
