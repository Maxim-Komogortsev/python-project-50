#!/usr/bin/env python3

from json import dumps


def format_diff_to_json(data):
    '''Formates data with json format'''
    json_data = dumps(data, indent=4, sort_keys=True)
    return json_data
