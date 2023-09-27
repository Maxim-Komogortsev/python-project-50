#!/usr/bin/env python3


from json import loads as json_load
from yaml import safe_load as yaml_load
from os.path import splitext


def get_format(file_path):
    '''Gets formats of the file'''
    file_ext = splitext(file_path)[1]
    return file_ext.lstrip('.')


def parse(data, data_format):
    '''Turns json or yaml data into python object'''
    if data_format == 'json':
        return json_load(data)
    elif data_format in ('yaml', 'yml'):
        return yaml_load(data)
    else:
        raise Exception("Invalid format for the file")


def get_data(file_path):
    '''Reads data from the file'''
    data_format = get_format(file_path)
    with open(file_path) as f:
        data = f.read()
    return parse(data, data_format)
