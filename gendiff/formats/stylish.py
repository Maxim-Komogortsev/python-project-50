#!usr/bin/env python3

from gendiff.decoder import decode

statuses = {
    'unchanged': '  {key}: {value}\n',
    'removed': '- {key}: {value}\n',
    'added': '+ {key}: {value}\n',
    'nested': '  {key}: {value}\n',
    'changed': ''
}


def format_diff_to_stylish(data):
    string_data = make_stylish_represent(data)
    return string_data


def make_stylish_represent(data, nest_lvl=0):
    string_data = '{\n'
    for node in data:
        node_type, values = data[node]
        added_status = statuses[node_type]
        spaces_before = trans_lvl_to_spaces(nest_lvl) * ' '
        spaces_after = (trans_lvl_to_spaces(nest_lvl) - 2) * ' '
        if isinstance(values, tuple):
            val1, val2 = values
            added_status1 = statuses['removed']
            added_status2 = statuses['added']
            string_line = ''.join([
                spaces_before,
                added_status1.format(
                    key=node,
                    value=style_value(val1, nest_lvl),
                ),
                spaces_before,
                added_status2.format(
                    key=node,
                    value=style_value(val2, nest_lvl),
                )
            ])

        else:
            if node_type == 'nested':
                values = make_stylish_represent(values, nest_lvl=nest_lvl + 1)
            string_line = ''.join([
                spaces_before,
                added_status.format(
                    key=node,
                    value=style_value(values, nest_lvl)
                )
            ])
        string_data = ''.join([string_data, string_line])
    string_data = ''.join([string_data, spaces_after, '}'])
    return string_data


def style_value(value, nest_lvl):
    if isinstance(value, dict):
        new_nest_lvl = nest_lvl + 1
        spaces_before = trans_lvl_to_spaces(new_nest_lvl) * ' '
        spaces_after = (trans_lvl_to_spaces(new_nest_lvl) - 2) * ' '
        added_status = statuses['unchanged']
        string_data = '{\n'
        for node in value:
            string_line = ''.join([
                spaces_before,
                added_status.format(
                    key=node,
                    value=style_value(value[node], nest_lvl=new_nest_lvl)
                )
            ])
            string_data = ''.join([string_data, string_line])
        string_data = ''.join([string_data, spaces_after, '}'])
        return string_data
    else:
        return decode(value)


def trans_lvl_to_spaces(nest_lvl):
    space_count = 2 + nest_lvl * 4
    return space_count
