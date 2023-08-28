import argparse
from pathlib import Path
import json


BASEDIR: Path = Path(__file__).parent.parent

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file)
     


def json_load(path):
    fname = Path(path).resolve()
    with open(fname) as f:
        json_obj = json.load(f)
    return json_obj
        
def generate_diff(file1, file2):
    data1 = json_load(file1)
    data2 = json_load(file2)
    agregate_data = data1.keys() | data2.keys()
    sorted_data = sorted(agregate_data, key=lambda x: x[0])
    strout = '{\n'
    for i in sorted_data:

        if i in data1 and i in data2:
            if data1[i] != data2[i]:
                strout += f' - {i}: {data1[i]}\n'\
                        f' + {i}: {data2[i]}\n'
            else:
                strout += f'   {i}: {data1[i]}\n'
            continue

        if i in data1:
            strout += f' - {i}: {data1[i]}\n'
        
        if i in data2:
            strout += f' + {i}: {data2[i]}\n'

    strout += '}'
    
    return strout
        

if __name__ == '__main__':
    main()