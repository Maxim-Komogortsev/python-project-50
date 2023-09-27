#!/usr/bin/env pyhton3

import pytest
from gendiff.gen_diff import generate_diff

FILE1_JSON = './tests/fixtures/structured_file1.json'
FILE2_JSON = './tests/fixtures/structured_file2.json'
FILE1_YAML = './tests/fixtures/structured_file1.yaml'
FILE2_YAML = './tests/fixtures/structured_file2.yaml'
FIX_STYLISH = './tests/fixtures/structured_expected.txt'
FIX_PLAIN = './tests/fixtures/plain_expected.txt'
FIX_JSON = './tests/fixtures/json_expected.txt'


@pytest.mark.parametrize(
    "fixture, file1, file2, style",
    [
        (FIX_STYLISH, FILE1_JSON, FILE2_JSON, 'stylish'),
        (FIX_PLAIN, FILE1_JSON, FILE2_JSON, 'plain'),
        (FIX_JSON, FILE1_JSON, FILE2_JSON, 'json'),
        (FIX_STYLISH, FILE1_YAML, FILE2_YAML, 'stylish'),
        (FIX_PLAIN, FILE1_YAML, FILE2_YAML, 'plain'),
        (FIX_JSON, FILE1_YAML, FILE2_YAML, 'json'),
        (FIX_STYLISH, FILE1_YAML, FILE2_JSON, 'stylish'),
        (FIX_PLAIN, FILE1_JSON, FILE2_YAML, 'plain'),
        (FIX_JSON, FILE1_YAML, FILE2_JSON, 'json'),
    ]
)
def test_style(fixture, file1, file2, style):
    with open(fixture, 'r') as fixture:
        expected = fixture.read()
    assert expected[:-1] == generate_diff(
        file1, file2, output_format=style
    )
