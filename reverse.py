import argparse

parser = argparse.ArgumentParser(description='reverse input file content and save it in out file')
parser.add_argument('in_file', help='input file')
parser.add_argument('--out_file', default='out.txt', help='output file')

args = parser.parse_args()
try:
    with open(args.in_file) as in_file:
        with open(args.out_file, 'w') as out_file:
            out_file.write(in_file.read()[-1::-1])
except FileNotFoundError:
    print('Файл не найден')
