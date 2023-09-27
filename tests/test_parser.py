from gendiff.parser import get_format, parse

file_path_json = '/home/User/file.json'
file_path_empty = '/home/User/'


def test_format():
    assert get_format(file_path_json) == 'json'
    assert get_format(file_path_empty) == ''


def test_parser_json():
    with open('./tests/fixtures/file1.json', 'r') as f:
        data = f.read()
    py_obj = parse(data, 'json')
    assert isinstance(py_obj, dict)


def test_parser_yaml():
    with open('./tests/fixtures/file1.yaml', 'r') as f:
        data = f.read()
    py_obj = parse(data, 'yaml')
    assert isinstance(py_obj, dict)
