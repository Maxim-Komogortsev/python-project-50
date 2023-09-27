#!/usr/bin/env python3


from gendiff.formats.json import format_diff_to_json
from gendiff.formats.stylish import format_diff_to_stylish
from gendiff.formats.plain import format_diff_to_plain


def format(diff, style):
    '''Chooses the format'''
    if style == 'json':
        formatted_diff = format_diff_to_json(diff)
    if style == 'stylish':
        formatted_diff = format_diff_to_stylish(diff)
    if style == 'plain':
        formatted_diff = format_diff_to_plain(diff)
    return formatted_diff
