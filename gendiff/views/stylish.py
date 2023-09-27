"""Stylish view returns json-like string of diff contents.

EXAMPLE
>>> generate_diff(before, after, 'stylish')
{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: True
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
      - setting6: {
            key: value
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}
"""

from collections import OrderedDict
from gendiff import diff

status_maps = {
    diff.UNCHANGED: "{ind}  {key}: {val}\n",
    diff.ADDED: "{ind}+ {key}: {val}\n",
    diff.DELETED: "{ind}- {key}: {val}\n",
    diff.CHANGED: "{ind}- {key}: {before}\n{ind}+ {key}: {after}\n"
}

first_line = "{ind}{sign} {key}: {{\n"

def correct_yml(v):
    if type(v) == bool:
        return str(v).lower()
    if v == None:
        return 'null'

    return v

def render_value(val, indent = 0) -> str:
    if isinstance(val, dict):
        ind = '  ' * indent
        closing_bracket = '  ' * (indent - 1)
        temp = []
        for ke, va in val.items():
            va = correct_yml(va)
            temp.append("{ind}  {key}: {val}\n".format(
                ind=ind, key=ke, val=va))
        conts = ''.join(temp)
        res = "{{\n{conts}{ind}}}".format(conts=conts, ind=closing_bracket)
        return res
    
    val = correct_yml(val)

    return val


def stylish_view(dif, depth=1) -> list:
    res = []
    ind = '  ' * depth
    for k, v in dif.items():
        status, *values = v
        if status == diff.NESTED:
            res.append("{ind}  {key}: {{\n".format(ind=ind, key=k))
            res += stylish_view(values[0], depth + 2)
            res.append(ind * 2 + "}\n")
        elif status == diff.CHANGED:
            pre = render_value(values[0])
            after = render_value(values[1])
            res.append(status_maps[status].format(
                ind=ind, key=k,
                before=pre, after=after))
        else:
            val = render_value(values[0], depth + 2)
            res.append(status_maps[status].format(
                ind=ind, key=k, val=val))
    return res


def render(diff) -> str:
    contents = ''.join(stylish_view(diff))
    string = "{{\n{contents}}}".format(contents=contents)
    return string


if __name__ == '__main__':
    test_di = {
        'Pls': True
    }
    print(render(OrderedDict([('key', ('C', True, False)), ('seckey', ('A', 12))])))
