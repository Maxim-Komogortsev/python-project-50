#!/usr/bin/env python3


from gendiff.parser import get_data
from gendiff.formats.formatter import format
from gendiff.formats.plain import sort_data


def diff_dict(  # noqa: C901
        data1, data2):
    keys1 = set(data1)
    keys2 = set(data2)
    keys = keys1 | keys2
    diff = dict()
    for key in keys:
        if key in data1 and key not in data2:
            value1 = data1[key]
            diff.update({key: ['removed', value1]})
        elif key not in data1 and key in data2:
            value2 = data2[key]
            diff.update({key: ['added', value2]})
        # all the other keys are present in both datas
        elif data1[key] == data2[key]:
            value1 = data1[key]
            diff.update({key: ['unchanged', value1]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            value1 = data1[key]
            value2 = data2[key]
            diff.update({key: ['nested', diff_dict(value1, value2)]})
        else:
            value1 = data1[key]
            value2 = data2[key]
            diff.update({key: ['changed', (value1, value2)]})
    return sort_data(diff)


def generate_diff(file_path1, file_path2, output_format='stylish'):
    '''Generates the formatted diff of two data'''
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = diff_dict(data1, data2)
    formatted_diff = format(diff, output_format)
    return formatted_diff
